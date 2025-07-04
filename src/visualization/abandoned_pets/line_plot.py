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
    district_name AS 자치구명,
    abandonment_count_2016,
    abandonment_count_2017,
    abandonment_count_2018,
    abandonment_count_2019,
    abandonment_count_2020
FROM seoul_abandonment_statistics
"""
df = pd.read_sql(query, engine)

# ▶️ 연도 기준으로 Melt
df_melted = pd.melt(df,
    id_vars=["자치구명"],
    value_vars=[
        "abandonment_count_2016",
        "abandonment_count_2017",
        "abandonment_count_2018",
        "abandonment_count_2019",
        "abandonment_count_2020"
    ],
    var_name="연도",
    value_name="유기견_건수"
)

# ▶️ '연도' 컬럼 숫자로 변환
df_melted["연도"] = df_melted["연도"].str.extract(r'(\d{4})').astype(int)

# ▶️ 시각화 (자치구별 연도별 유기견 발생 추이)
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_melted, x="연도", y="유기견_건수", hue="자치구명", marker='o')
plt.title("✅ 자치구별 연도별 유기동물 발생 추이 (2016~2020)", fontsize=16)
plt.ylabel("유기견 건수")
plt.xlabel("연도")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/자치구별_연도별_유기동물_발생_추이_(2016~2020).png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()