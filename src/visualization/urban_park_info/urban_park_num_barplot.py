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
load_dotenv("/home/jiming/dev_ws/eda-repo-3/env")

# 환경 변수 가져오기
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▶️ MySQL 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# ▶️ 전국 도시 공원 지역 정보 가져오기
# 서울 관련 정보만 가져오기
query = """
SELECT jibun_address as 주소, latitude as 위도, longitude as 경도, park_area as 면적, provider_name as 제공처
FROM korea_urban_park_info
WHERE jibun_address like "%%서울%%"
"""
df = pd.read_sql(query, engine)

df.columns =['주소', '위도', '경도', '면적', '제공처']

# 자치구별로 구분하기
df['자치구'] = df['제공처'].str.extract(r'서울특별시\s+(\S+구)')


df_grouped = df.groupby('자치구').size().reset_index(name ='count')

df_sorted = df_grouped.sort_values(by='count', ascending=False)
df_sorted.columns = ['자치구', '공원 수']
print(df_sorted)

# # 시각화
plt.figure(figsize=(14,8))
ax = sns.barplot(data=df_sorted, x='자치구', y='공원 수')

# ▶️ 수치 레이블 추가
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=9, padding=3)


sns.barplot(data=df_sorted, x='자치구', y='공원 수')
plt.title('서울시 자치구별 공원 수', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('자치구')
plt.ylabel('공원 수')
plt.tight_layout()



# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/서울시_공원총개수_막대그래프.png'
# os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()