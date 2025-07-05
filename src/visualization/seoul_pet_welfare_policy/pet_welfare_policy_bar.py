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
load_dotenv('env')
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▒ DB 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# ▒ 데이터 조회
query = """
SELECT *
FROM seoul_pet_welfare_policy
"""
df = pd.read_sql(query, engine)
df = df.drop(columns=['created_at'])

df['num_sum'] = df[['animal_shelter_in_district', 'dog_playground_or_shelter', 'pet_behavior_education', 'stray_cat_feeding_station', 'low_income_vet_support', 'pet_temporary_care']].sum(axis=1)

df_total = df[['district_name', 'num_sum']]
print(df_total)

df_total_park = df[['district_name', 'num_sum']]
df_sorted_3 = df_total_park.sort_values(by='num_sum', ascending=False)
plt.figure(figsize=(14,8))
ax = sns.barplot(data=df_sorted_3, x='district_name', y='num_sum')

# ▶️ 수치 레이블 추가
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=9, padding=3)

plt.title("서울시 반려동물 지원정책 총 개수", fontsize=16)
plt.ylabel("num_sum")
plt.xlabel("district_name")
plt.xticks(rotation=45)
plt.tight_layout()


# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/서울시_반려동물_지원정책_총합.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장
plt.show()
