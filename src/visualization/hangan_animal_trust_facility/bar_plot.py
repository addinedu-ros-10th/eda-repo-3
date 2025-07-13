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



# ▶️ 서울 동물위탁관리업 관련 인허가 정보 가져오기
  # 영업/정상 : 필터링
  # 서울특별시 : 지역으로 필터링
  
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

# ▶️ 시각화 (자치구별 동물위탁관리업 추이)
plt.figure(figsize=(14, 8))
plt.bar(district_counts['district'], district_counts['animal_trust_count'])
plt.title("✅ 자치구별 동물위탁관리업 현황 2024", fontsize=16)
plt.xlabel("자치구(서울)")
plt.ylabel("동물위탁관리업 수")
plt.grid(True, linestyle='--', alpha=0.6)
# plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
# plt.tight_layout()
# plt.show()

save_dir = os.path.expanduser('~/eda-repo-3/RESULT/visualization')
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

plt.savefig(os.path.join(save_dir, "행정안전부_서울시_동물위탁관리업_막대그래프.png"))