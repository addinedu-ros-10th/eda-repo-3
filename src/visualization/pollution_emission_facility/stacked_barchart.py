import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
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
	*
FROM pollution_emission_facility
WHERE region_small != '소계'
"""
df = pd.read_sql(query, engine)

# 한글 alias 설정
aliases = {
    "air_total": "대기배출시설",
    "water_total": "수질배출시설",
    "noise_total": "소음진동시설"
}

# 시각화용 정제 및 정렬
df_chart = df[["region_small", "air_total", "water_total", "noise_total"]]
df_chart = df_chart.sort_values(by=["air_total", "water_total", "noise_total"], ascending=False)

# 누적 막대 그래프
plt.figure(figsize=(16, 8))
plt.bar(df_chart["region_small"], df_chart["air_total"], label=aliases["air_total"])
plt.bar(df_chart["region_small"], df_chart["water_total"], bottom=df_chart["air_total"], label=aliases["water_total"])
plt.bar(df_chart["region_small"],
        df_chart["noise_total"],
        bottom=df_chart["air_total"] + df_chart["water_total"],
        label=aliases["noise_total"])

# 누적 수치 표시
for i in range(len(df_chart)):
    total = df_chart.iloc[i][["air_total", "water_total", "noise_total"]].sum()
    plt.text(i, total + 5, str(total), ha='center', fontsize=8)

plt.title("자치구별 환경오염물질 배출시설 현황 (누적)", fontsize=14)
plt.xlabel("자치구")
plt.ylabel("시설 수")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid(axis='y')


# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/자치구별_환경오염물질_배출시설_현황_(누적).png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()

