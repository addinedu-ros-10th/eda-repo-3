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

# ▒ 데이터 조회
query = """
SELECT road_address, jibun_address
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

# ▒ 자치구 컬럼 생성
df['자치구'] = df['road_address'].apply(extract_district)
df['자치구'] = df['자치구'].fillna(df['jibun_address'].apply(extract_district))

print(df)

# ▒ 병원 수 집계
district_count = df['자치구'].value_counts().reset_index()
district_count.columns = ['자치구', '병원 수']
district_count = district_count.sort_values(by='병원 수', ascending=False)

# ▒ 시각화 (단일 막대)
plt.figure(figsize=(14, 8))
sns.barplot(data=district_count, x='자치구', y='병원 수', palette='Set3')

# ▒ 수치 표시
for index, row in district_count.iterrows():
    plt.text(index, row['병원 수'] + 1, row['병원 수'], ha='center', va='bottom', fontsize=9)

plt.title("서울시 자치구별 동물병원 수", fontsize=16)
plt.ylabel("병원 수")
plt.xlabel("자치구")
plt.xticks(rotation=45)
plt.tight_layout()

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/서울시_자치구별_동물병원_수_막대그래프.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()