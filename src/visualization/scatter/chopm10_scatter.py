import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import platform

# 한글 폰트 설정
if platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
elif platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# .env 환경변수 로드
load_dotenv('env')
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# DB 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

query1 = """
SELECT station_name, annual_average
FROM pollution_pm10_concentration_by_station
WHERE province LIKE '서울'
"""

query2 = """
SELECT station_name, annual_avg
FROM pollution_pm25_concentration_by_station
WHERE province LIKE '서울'
"""

df_10 = pd.read_sql(query1, engine)
df_10.rename(columns={'station_name': '자치구', 'annual_average': '미세먼지 농도'}, inplace=True)

df_25 = pd.read_sql(query2, engine)
df_25.rename(columns={'station_name': '자치구', 'annual_avg': '초미세먼지 농도'}, inplace=True)

df_dust = pd.merge(df_10, df_25, on='자치구', how='outer')

# csv 불러오기
input_path = os.path.join('RESULT', 'csv', 'seoul_integrated_data.csv')
df = pd.read_csv(input_path)

df_companion = df.iloc[:, [0, 1]].copy()
df_companion.rename(columns={
    'district': '자치구',
    'companion_animal_registration': '반려동물 등록수'
}, inplace=True)

df_merge = pd.merge(df_companion, df_dust, on='자치구', how='outer')

# 초미세먼지 농도 기준 top5, bottom5
top5 = df_merge.nlargest(5, '초미세먼지 농도')
bottom5 = df_merge.nsmallest(5, '초미세먼지 농도')
middle = df_merge[~df_merge['자치구'].isin(top5['자치구']) & ~df_merge['자치구'].isin(bottom5['자치구'])]

plt.figure(figsize=(14, 7))

# 중간 그룹
sns.scatterplot(data=middle, x='반려동물 등록수', y='초미세먼지 농도', label='중간', color='gray')

# Top5
sns.scatterplot(data=top5, x='반려동물 등록수', y='초미세먼지 농도', label='초미세먼지 농도 상위 5개', color='blue')

# Bottom5
sns.scatterplot(data=bottom5, x='반려동물 등록수', y='초미세먼지 농도', label='초미세먼지 농도 하위 5개', color='red')

# 회귀선 + 신뢰구간
sns.regplot(data=df_merge, x='반려동물 등록수', y='초미세먼지 농도',
            scatter=False, color='black',
            line_kws={"linestyle": "dashed"}, label='회귀선')

# 자치구 이름 라벨 표시 (라벨 겹침 주의, 필요 시 위치 조절)
# 자치구 이름 라벨 표시 (45도 회전)
for i in range(df_merge.shape[0]):
    plt.annotate(df_merge.loc[i, '자치구'], 
                 (df_merge.loc[i, '반려동물 등록수'] + 100, df_merge.loc[i, '초미세먼지 농도']),
                 fontsize=9,
                 rotation=45,
                 ha='right',
                 va='center')

plt.xlabel('반려동물 등록수')
plt.ylabel('초미세먼지 농도 (연평균)')
plt.title('서울 자치구별 반려동물 등록수와 초미세먼지 농도 산점도')
plt.grid(True)
plt.legend()
plt.tight_layout()

output_path = 'RESULT/visualization/등록수_VS_초미세먼지_회귀선포함_scatter.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')

plt.show()
