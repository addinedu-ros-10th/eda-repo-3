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
load_dotenv('env')

# 환경 변수 가져오기
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▶️ MySQL 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")



# ▶️ 서울 동물미용업 관련 인허가 정보 가져오기
  # 영업/정상 : 필터링
  # 서울특별시 : 지역으로 필터링
  
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



import matplotlib.pyplot as plt
import pandas as pd

# 데이터프레임 세팅
district_counts.columns = ['district', 'beauty_count']

# 박스플롯
plt.figure(figsize=(8, 12))
plt.boxplot(district_counts['beauty_count'], vert=True)
plt.title('서울시 시군구별 미용업체 수 분포 (beauty_count)')
plt.ylabel('미용업체 수')

# 산점도 위에 district 별 값 표시
x = [1] * len(district_counts)
y = district_counts['beauty_count']

plt.scatter(x, y, color='red')

# 점 옆에 시군구 라벨 표시
for i, txt in enumerate(district_counts['district']):
    plt.text(1.05, y.iloc[i], txt, fontsize=8, verticalalignment='center')

plt.grid(True)



# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/동물미용업_boxplot.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()