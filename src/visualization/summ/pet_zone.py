# ===========================================

# 과연 반려동물 업장은 몰려있을까 AND 반려동물 등록수가 높은가

# ===========================================

import matplotlib
matplotlib.use('TkAgg')
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


# ▶️ 미용실 ========================================
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
df_merged = pd.merge(df_beauty, df_hospital,  on='district', how='inner')
df_merged = pd.merge(df_merged,df_pharmacy, on='district', how='inner')
df_merged = pd.merge(df_merged, df_hotel, on='district', how='inner')

df_merged_sorted = df_merged.sort_values(by='district', ascending=True)
df_merged_sorted['total_facilities'] = df_merged_sorted[['beauty_count', 'hospital_count', 'pharmacy_count', 'animal_trust_count']].sum(axis=1)



#시각화 ================================================

plt.figure(figsize=(16,8))

x = df_merged_sorted['district']

# 막대그래프 (total_facilities)
plt.bar(x, df_merged_sorted['total_facilities'], color='#4e79a7', alpha=0.6, label='총 시설 수')

# 꺾은선 그래프 (미용실, 병원, 약국, 위탁관리업)
plt.plot(x, df_merged_sorted['beauty_count'], marker='o', label='미용실 수')
plt.plot(x, df_merged_sorted['hospital_count'], marker='s', label='병원 수')
plt.plot(x, df_merged_sorted['pharmacy_count'], marker='^', label='약국 수')
plt.plot(x, df_merged_sorted['animal_trust_count'], marker='D', label='위탁관리업 수')

plt.xticks(rotation=45)
plt.xlabel('자치구')
plt.ylabel('시설 수')
plt.title('서울시 자치구별 동물 관련 시설 현황')

plt.legend()
plt.tight_layout()
plt.show()


