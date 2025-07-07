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

df_total_park = df[['자치구', '1인당 도보생활권공원 면적']]
df_sorted_3 = df_total_park.sort_values(by='1인당 도보생활권공원 면적', ascending=False)


# 박스플롯 ==================================
plt.figure(figsize=(8, 12))
plt.boxplot(df_sorted_3['1인당 도보생활권공원 면적'], vert=True)
plt.title('1인당 도보생활권공원 면적')
plt.ylabel('1인당 도보생활권공원 면적')

# 산점도 위에 district 별 값 표시
x = [1] * len(df_sorted_3)
y = df_sorted_3['1인당 도보생활권공원 면적']

plt.scatter(x, y, color='red')

# 점 옆에 시군구 라벨 표시
for i, txt in enumerate(df_sorted_3['자치구']):
    plt.text(1.05, y.iloc[i], txt, fontsize=8, verticalalignment='center')

plt.grid(True)


# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/1인당_도보생활권공원_면적_boxplot.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()
