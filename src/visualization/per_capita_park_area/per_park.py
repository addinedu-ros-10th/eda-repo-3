# ====================================================

# 공원 (모든 공원 다 의미함)
# 도시공원 ( 도시 내 설치된 공원만 )
# 도보 생활권 공원 ( 도보로 10분 내 접근 가능한 공원 )

# ====================================================

import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import folium
from sqlalchemy import create_engine
from shapely.geometry import shape
from io import BytesIO
import base64
import seaborn as sns

from dotenv import load_dotenv
import os
import json


# .env 파일을 찾아 환경 변수로 로드
load_dotenv("env")

# 환경 변수 가져오기
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▶️ MySQL 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# ▶️ 공원 정보 가져오기
query = """
SELECT district_category_2, per_capita_park_area_sqm, per_capita_urban_park_area_sqm, per_capita_walkable_park_area_sqm
FROM per_capita_park_area
WHERE district_category_2  not like "서울대공원"
ORDER BY district_category_2;
"""
df = pd.read_sql(query, engine)
df.columns =['자치구', '1인당 공원 면적', '1인당 도시공원 면적', '1인당 도보생활권공원 면적']


# =============================
# 시각화1 _ 1인당 공원 면적
# =============================

df_total_park = df[['자치구', '1인당 공원 면적']]
df_sorted_1 = df_total_park.sort_values(by='1인당 공원 면적', ascending=False)
plt.figure(figsize=(14,8))
ax = sns.barplot(data=df_sorted_1, x='자치구', y='1인당 공원 면적')

# ▶️ 수치 레이블 추가
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', label_type='edge', fontsize=9, padding=3)


sns.barplot(data=df_sorted_1, x='자치구', y='1인당 공원 면적')
plt.title('서울시 자치구별 1인당 공원 면적', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('자치구')
plt.ylabel('1인당 공원 면적(m^2)')
plt.tight_layout()

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/서울시_1인당_공원면적_막대그래프.png'
# os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()


# ================================
# 시각화2 _ 1인당 도시공원
# ================================

df_total_park = df[['자치구', '1인당 도시공원 면적']]
df_sorted_2 = df_total_park.sort_values(by='1인당 도시공원 면적', ascending=False)
plt.figure(figsize=(14,8))
ax = sns.barplot(data=df_sorted_2, x='자치구', y='1인당 도시공원 면적')

# ▶️ 수치 레이블 추가
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', label_type='edge', fontsize=9, padding=3)


sns.barplot(data=df_sorted_2, x='자치구', y='1인당 도시공원 면적')
plt.title('서울시 자치구별 1인당 도시공원 면적', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('자치구')
plt.ylabel('1인당 도시공원 면적(m^2)')
plt.tight_layout()

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/서울시_1인당_도시공원_면적_막대그래프.png'
# os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()

# ================================
# 시각화3 _ 1인당 도보생활권공원
# ================================

df_total_park = df[['자치구', '1인당 도보생활권공원 면적']]
df_sorted_3 = df_total_park.sort_values(by='1인당 도보생활권공원 면적', ascending=False)
plt.figure(figsize=(14,8))
ax = sns.barplot(data=df_sorted_3, x='자치구', y='1인당 도보생활권공원 면적')

# ▶️ 수치 레이블 추가
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', label_type='edge', fontsize=9, padding=3)


sns.barplot(data=df_sorted_3, x='자치구', y='1인당 도보생활권공원 면적')
plt.title('서울시 자치구별 1인당 도보생활권공원 면적', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('자치구')
plt.ylabel('1인당 도보생활권공원 면적(m^2)')
plt.tight_layout()

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/서울시_1인당_도보생활권공원_면적_막대그래프.png'
# os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()
