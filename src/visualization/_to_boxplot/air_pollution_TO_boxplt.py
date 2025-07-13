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
load_dotenv('env')
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
df_chart["total"] = df_chart[["air_total", "water_total", "noise_total"]].sum(axis=1)
df_chart = df_chart.sort_values(by="total", ascending=False)

# 박스플롯 ======================================================
plt.figure(figsize=(8, 12))
plt.boxplot(df_chart['total'], vert=True)
plt.title('환경 오염 요인 총합')
plt.ylabel('환경 오염 요인 총합')

# 산점도 위에 district 별 값 표시
x = [1] * len(df_chart)
y = df_chart['total']

plt.scatter(x, y, color='red')

# 점 옆에 시군구 라벨 표시
for i, txt in enumerate(df_chart['region_small']):
    plt.text(1.05, y.iloc[i], txt, fontsize=8, verticalalignment='center')

plt.grid(True)

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/환경오염요인_총합_boxplot.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()