import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import folium
from sqlalchemy import create_engine
from shapely.geometry import shape
from io import BytesIO
import base64

from dotenv import load_dotenv
import os
import json

# .env 파일을 찾아 환경 변수로 로드
load_dotenv()

# 환경 변수 가져오기
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▶️ MySQL 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")



# ▶️ seoul_abandoned_animal_status 등록 데이터 가져오기
query = """
SELECT *
FROM seoul_abandoned_animal_status
"""
df = pd.read_sql(query, engine)
# 개 / 고양이 유기동물 발생 합계 계산
# 개 / 고양이 안락사 발생 합계 계산

# 0번행(총계) 제거
df.drop(0, inplace=True)

# 구별 개수 집계
df['abandon_count'] = df['dog_total'] + df['cat_total']
df['deceased_count'] = df['dog_deceased'] + df['cat_deceased']

# 2. 구별 유기동물/안락사 합계 집계
abandon_counts = df.groupby('district_level_2')['abandon_count'].sum().reset_index()
abandon_counts = abandon_counts.sort_values('abandon_count', ascending=False)

deceased_counts = df.groupby('district_level_2')['deceased_count'].sum().reset_index()
deceased_counts = deceased_counts.sort_values('deceased_count', ascending=False)


# ▶️ 시각화 (자치구별 유기동물 발생 추이)
plt.figure(figsize=(14, 8))
bar = plt.bar(abandon_counts['district_level_2'], abandon_counts['abandon_count'])
# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1f' % height, ha='center', va='bottom', size = 12)

plt.title("자치구별 유기동물 발생 현황 2021", fontsize=16)
plt.xlabel("자치구(서울)")
plt.ylabel("유기동물 발생 현황")
plt.grid(True, linestyle='--', alpha=0.6)

save_dir = os.path.expanduser('~/eda-repo-3/RESULT/visualization')
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

plt.savefig(os.path.join(save_dir, "서울시_자치구별_유기동물_막대그래프.png"))

# ▶️ 시각화 (자치구별 반려동물 안락사 발생 추이)
plt.figure(figsize=(14, 8))
bar = plt.bar(deceased_counts['district_level_2'], deceased_counts['deceased_count'])


# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1f' % height, ha='center', va='bottom', size = 12)


plt.title("자치구별 반려동물 안락사 발생 현황 2021", fontsize=16)
plt.xlabel("자치구(서울)")
plt.ylabel("반려동물 안락사 발생 현황")
plt.grid(True, linestyle='--', alpha=0.6)

plt.savefig(os.path.join(save_dir, "서울시_자치구별_안락사동물_막대그래프.png"))
# plt.show()
