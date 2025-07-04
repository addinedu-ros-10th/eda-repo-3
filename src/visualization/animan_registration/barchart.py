import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# ▶️ .env 파일의 환경변수 불러오기
load_dotenv()
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▶️ MySQL 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# ▶️ 데이터 조회
query = """
SELECT 
    sido as 시도,
    sigungu as 시군구,
    dog_registered_total as 개등록_누계,
    cat_registered_total as 고양이등록_누계,
    total_registered as 총등록_누계
FROM companion_animal_registration
WHERE sido = '서울특별시'
ORDER BY total_registered DESC
"""
df = pd.read_sql(query, engine)

df.columns = ['시도', '시군구', '개등록_누계', '고양이등록_누계', '총등록_누계']

# 다중 막대 그래프용 데이터 전처리
df_melted = df.melt(id_vars=['시군구'], 
                    value_vars=['개등록_누계', '고양이등록_누계'],
                    var_name='종류', value_name='등록수')

# 시각화
plt.figure(figsize=(14, 8))

ax = sns.barplot(data=df_melted, x='시군구', y='등록수', hue='종류')

# ▶️ 수치 레이블 추가
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=9, padding=3)


# sns.barplot(data=df_melted, x='시군구', y='등록수', hue='종류')
plt.title('서울시 자치구별 반려동물 등록 수 (개/고양이)', fontsize=16)
plt.ylabel('등록 개체수')
plt.xticks(rotation=45)
plt.tight_layout()

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/서울시_반려동물등록_막대그래프.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()