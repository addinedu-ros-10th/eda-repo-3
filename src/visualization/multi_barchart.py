import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import re
import platform


# ▒ 한글 폰트 설정
if platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
elif platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# ▶️ .env 파일의 환경변수 불러오기
load_dotenv()
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▶️ MySQL 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# ▒ 업태별 자치구 병원 수 집계
query = """
SELECT road_address, jibun_address, category_name
FROM seoul_animal_hospital
WHERE status_name in ('영업/정상')  -- 폐업 제외
"""
df = pd.read_sql(query, engine)

# ▒ 자치구 추출 함수
def extract_district(address):
    # match = re.search(r'서울\s*(\S+구)', str(address))
    # return match.group(1) if match else None
    if address:
        return address.split(' ')[1]
    else:
        None

# ▒ 자치구 추출
df['자치구'] = df['road_address'].apply(extract_district)
df['자치구'] = df['자치구'].fillna(df['jibun_address'].apply(extract_district))

# ▒ null 제거
df = df.dropna(subset=['자치구', 'category_name'])

# ▒ 그룹화
grouped = df.groupby(['자치구', 'category_name']).size().reset_index(name='병원 수')

# ▒ 시각화 (다중 막대)
plt.figure(figsize=(16, 9))
sns.barplot(data=grouped, x='자치구', y='병원 수', hue='category_name')
plt.title("서울시 자치구별 업태별 동물병원 수", fontsize=16)
plt.xticks(rotation=45)
plt.ylabel("병원 수")
plt.xlabel("자치구")
plt.legend(title='업태구분')
plt.tight_layout()
plt.show()
