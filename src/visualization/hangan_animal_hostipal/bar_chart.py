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


# ▶️ 서울 동물병원 정보 가져오기
  # 영업/정상
  # 서울특별시
  
  # 영업상태명 / 소재지전체주소 / 도로명우편번호 / 사업장명
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

# ▶️ 시각화 (자치구별 연도별 유기견 발생 추이)
plt.figure(figsize=(14, 8))
plt.bar(district_counts['district'], district_counts['hospital_count'])
plt.title("✅ 자치구별 동물병원 현황 2024", fontsize=16)
plt.xlabel("자치구(서울)")
plt.ylabel("동물병원 수")
plt.grid(True, linestyle='--', alpha=0.6)
# plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
# plt.tight_layout()
# plt.show()

plt.savefig("RESULT/visualization/서울시_동물병원수_막대그래프.png")
