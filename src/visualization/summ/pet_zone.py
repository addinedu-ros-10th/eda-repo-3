# ===========================================

# 과연 반려동물 업장은 몰려있을까 AND 반려동물 등록수가 높은가

# ===========================================


import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# ▶️ .env 파일의 환경변수 불러오기
load_dotenv("/home/jiming/dev_ws/eda-repo-3/env")
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▶️ MySQL 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")


# 반려동물 등록수 ======================================
query = """
SELECT 
    sigungu as 시군구,
    total_registered as 총등록_누계
FROM companion_animal_registration
WHERE sido = '서울특별시'
ORDER BY total_registered DESC
"""
df_register = pd.read_sql(query, engine)

df_register.columns = ['시군구','총등록_누계']




# ▶️ 미용실 ========================================
query = """
SELECT *
FROM animal_beauty_business
WHERE (status_name LIKE '영업/정상') AND (address_jibun LIKE '서울특별시%%')
"""
df = pd.read_sql(query, engine)

# 구 이름 추출 방법 1: 문자열 분할
df['district'] = df['address_jibun'].str.split(' ').str[2]

# 구 이름 추출 방법 2: 정규표현식 사용
import re
df['district'] = df['address_jibun'].str.extract(r'서울특별시 ([가-힣]+구)')

# 구별 개수 집계
district_counts = df['district'].value_counts().reset_index()
district_counts.columns = ['district', 'beauty_count']
district_counts = district_counts.sort_values('beauty_count', ascending=False)
df_beauty = district_counts



# ▶️ 병원 =======================================
query = """
SELECT jibun_address
FROM animal_hospital_registry
WHERE (status_name LIKE '영업/정상') AND (jibun_address LIKE '서울특별시%%')
"""
df = pd.read_sql(query, engine)

# 구 이름 추출 방법 1: 문자열 분할
df['district'] = df['jibun_address'].str.split(' ').str[2]

# 구 이름 추출 방법 2: 정규표현식 사용
import re
df['district'] = df['jibun_address'].str.extract(r'서울특별시 ([가-힣]+구)')

# 구별 개수 집계
district_counts = df['district'].value_counts().reset_index()
district_counts.columns = ['district', 'hospital_count']
district_counts = district_counts.sort_values('hospital_count', ascending=False)

df_hospital = district_counts

# ▶️ 약국 =======================================
query = """
SELECT *
FROM animal_pharmacy_registry
WHERE (status_name LIKE '영업/정상') AND (jibun_address LIKE '서울특별시%%')
"""
df = pd.read_sql(query, engine)

# 구 이름 추출 방법 1: 문자열 분할
df['district'] = df['jibun_address'].str.split(' ').str[2]

# 구 이름 추출 방법 2: 정규표현식 사용
import re
df['district'] = df['jibun_address'].str.extract(r'서울특별시 ([가-힣]+구)')

# 구별 개수 집계
district_counts = df['district'].value_counts().reset_index()
district_counts.columns = ['district', 'pharmacy_count']
district_counts = district_counts.sort_values('pharmacy_count', ascending=False)

df_pharmacy = district_counts


# ▶️ 위탁관리업 =======================================
query = """
SELECT *
FROM seoul_animal_trust_facility
WHERE (status_name LIKE '영업/정상') AND (jibun_address LIKE '서울특별시%%')
"""
df = pd.read_sql(query, engine)

# 구 이름 추출 방법 1: 문자열 분할
df['district'] = df['jibun_address'].str.split(' ').str[2]

# 구 이름 추출 방법 2: 정규표현식 사용
import re
df['district'] = df['jibun_address'].str.extract(r'서울특별시 ([가-힣]+구)')

# 구별 개수 집계
district_counts = df['district'].value_counts().reset_index()
district_counts.columns = ['district', 'animal_trust_count']
district_counts = district_counts.sort_values('animal_trust_count', ascending=False)


df_hotel = district_counts


# 데이터 병합하기 =============================================
df_plot = pd.merge(df_beauty, df_hospital,  on='district', how='inner')
df_plot = pd.merge(df_plot,df_pharmacy, on='district', how='inner')
df_plot = pd.merge(df_plot, df_hotel, on='district', how='inner')

df_merged_sorted = df_plot.sort_values(by='district', ascending=True)
df_merged_sorted['total_facilities'] = df_merged_sorted[['beauty_count', 'hospital_count', 'pharmacy_count', 'animal_trust_count']].sum(axis=1)



#시각화 ================================================
plt.figure(figsize=(16,8))

x = df_merged_sorted['district']

# 🔵 주 y축 (왼쪽) - 막대그래프
ax1 = plt.gca()
ax1.bar(x, df_register['총등록_누계'], color='#4e79a7', alpha=0.6, label='총 반려동물 등록 수')
ax1.set_ylabel('등록 수', color='#4e79a7')
ax1.tick_params(axis='y', labelcolor='#4e79a7')

# 🔴 보조 y축 (오른쪽) - 꺾은선 그래프
ax2 = ax1.twinx()
ax2.plot(x, df_plot['beauty_count'], marker='o', label='미용실 수', color='#f28e2c')
ax2.plot(x, df_plot['hospital_count'], marker='s', label='병원 수', color='#e15759')
ax2.plot(x, df_plot['pharmacy_count'], marker='^', label='약국 수', color="#1c38da")
ax2.plot(x, df_plot['animal_trust_count'], marker='D', label='위탁관리업 수', color='#59a14f')
ax2.set_ylabel('시설 수', color='gray')
ax2.tick_params(axis='y', labelcolor='gray')

# ✅ 공통 설정
plt.xticks(rotation=45)
ax1.set_xlabel('자치구')
plt.title('서울시 자치구별 반려동물 등록 수 및 동물 관련 시설 수')

# ✅ 범례 합치기
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

plt.tight_layout()
plt.show()

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/Sum_반려동물등록수AND시설전체.png'
# os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

