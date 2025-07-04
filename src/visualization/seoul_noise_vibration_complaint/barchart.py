import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# ▒ 한글 폰트 설정 (플랫폼별 처리)
import platform
if platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
elif platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# ▒ .env 환경변수 로드
load_dotenv()
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▒ DB 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# ▒ 데이터 조회
query = """
SELECT 
    district_level_2 AS 자치구,
    noise_vibration_complaint AS '소음·진동 민원',
    factory_noise_vibration_complaint AS '공장 소음·진동',
    traffic_noise_vibration_complaint AS '교통 소음·진동',
    life_noise_vibration_complaint AS '생활 소음·진동'
FROM seoul_noise_vibration_complaint
WHERE district_level_2 != '합계'
"""
df = pd.read_sql(query, engine)

# ▒ 자치구별 총 민원 수 기준 내림차순 정렬
df['총합'] = df[['공장 소음·진동', '교통 소음·진동', '생활 소음·진동']].sum(axis=1)
df = df.sort_values(by='총합', ascending=False)

# ▒ 시각화 - 누적 바차트
plt.figure(figsize=(16, 9))
bottom = None
categories = ['공장 소음·진동', '교통 소음·진동', '생활 소음·진동']

for cat in categories:
    plt.bar(df['자치구'], df[cat], label=cat, bottom=bottom)
    bottom = df[cat] if bottom is None else bottom + df[cat]

# ▒ 수치 표시
for i in range(len(df)):
    total = df.iloc[i][categories].sum()
    plt.text(i, total + 20, f'{total}', ha='center', va='bottom', fontsize=9)

plt.title('서울시 자치구별 소음·진동 민원 누적 현황', fontsize=16)
plt.xlabel('자치구')
plt.ylabel('민원 건수')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
