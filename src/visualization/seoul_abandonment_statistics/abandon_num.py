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

# ▶️ 유기동물 마리수 가져오기
query = """
SELECT *
FROM seoul_abandonment_statistics
ORDER BY district_name
"""
df = pd.read_sql(query, engine)
df.columns =['id','자치구', '2016', '2017', '2018', '2019', '2020', '삭제']

# 필요없는 column 제거하기
df = df.drop(columns =['id', '삭제'])

# 평균값 구하기
df['평균'] = df[['2016', '2017', '2018', '2019', '2020']].mean(axis=1)
print(df)

df_sorted = df.sort_values(by='평균', ascending=False)

# 시각화
plt.figure(figsize=(14,8))
ax = sns.barplot(data=df_sorted, x='자치구', y='평균')

# ▶️ 수치 레이블 추가
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=9, padding=3)


sns.barplot(data=df_sorted, x='자치구', y='평균')
plt.title('서울시 자치구별 평균 유기동물 수', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('자치구')
plt.ylabel('평균 유기동물 수')
plt.tight_layout()



# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/서울시_평균유기동물수_막대그래프.png'
# os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()