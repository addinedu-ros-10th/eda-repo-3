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
df_sorted = df.sort_values(by='평균', ascending=False)

df_final = df[['자치구', '평균']]



# 박스플롯
plt.figure(figsize=(8, 12))
plt.boxplot(df_final['평균'], vert=True)
plt.title('(평균) 유기동물 수')
plt.ylabel('평균 유기동물 수')

# 산점도 위에 district 별 값 표시
x = [1] * len(df_final)
y = df_final['평균']

plt.scatter(x, y, color='red')

# 점 옆에 시군구 라벨 표시
for i, txt in enumerate(df_final['자치구']):
    plt.text(1.05, y.iloc[i], txt, fontsize=8, verticalalignment='center')

plt.grid(True)

# 이미지 저장

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/유기동물수_boxplot.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()