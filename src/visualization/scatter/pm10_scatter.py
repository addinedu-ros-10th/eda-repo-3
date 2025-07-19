# import pandas as pd
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
# import seaborn as sns
# from sqlalchemy import create_engine
# from dotenv import load_dotenv
# import os

# # ▒ 한글 폰트 설정 (플랫폼별 처리)
# import platform
# if platform.system() == 'Darwin':
#     plt.rcParams['font.family'] = 'AppleGothic'
# elif platform.system() == 'Windows':
#     plt.rcParams['font.family'] = 'Malgun Gothic'
# else:
#     plt.rcParams['font.family'] = 'NanumGothic'
# plt.rcParams['axes.unicode_minus'] = False

# # ▒ .env 환경변수 로드
# load_dotenv('env')
# host = os.getenv("DB_HOST")
# user = os.getenv("DB_USER")
# password = os.getenv("DB_PASSWORD")
# database = os.getenv("DB_NAME")

# # ▒ DB 연결
# engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# query1 = """
# SELECT station_name, annual_average
# FROM pollution_pm10_concentration_by_station
# WHERE province LIKE '서울'
# """

# query2 = """
# SELECT station_name, annual_avg
# FROM pollution_pm25_concentration_by_station
# WHERE province LIKE '서울'
# """

# df_10 = pd.read_sql(query1, engine)
# df_10.rename(columns={'station_name' : '자치구',
#                    'annual_average' : '미세먼지 농도'},
#           inplace=True)


# df_25 = pd.read_sql(query2, engine)
# df_25.rename(columns={'station_name' : '자치구',
#                    'annual_avg' : '초미세먼지 농도'},
#           inplace=True)

# df_dust = pd.merge(df_10, df_25, on='자치구', how='outer')
# df_dust

# # ▶️ csv 불러오기 경로 지정
# input_path = os.path.join('RESULT','csv','seoul_integrated_data.csv')
# # input_path = 'RESULT/csv/seoul_integrated_data.csv'
# # os.path.dirname(output_path)
# df = pd.read_csv(input_path)

# df_companion = df.iloc[:, [0,1]]
# df_companion.rename(columns={
#   'district' : '자치구',
#   'companion_animal_registration' : '반려동물 등록수'}, inplace=True)
# df_companion

# df_merge = pd.merge(df_companion, df_dust, on='자치구', how='outer')
# df_merge

# # Assuming df_merge is the dataframe containing the relevant data
# plt.figure(figsize=(12, 6))
# plt.scatter(df_merge['반려동물 등록수'], df_merge['미세먼지 농도'], color='skyblue', alpha=0.7, edgecolors='black')

# # 각 점에 자치구 이름 라벨 표시
# for i, txt in enumerate(df_merge['자치구']):
#     plt.annotate(txt, 
#                  (df_merge['반려동물 등록수'].iloc[i], df_merge['미세먼지 농도'].iloc[i]), 
#                  fontsize=8, rotation=45, ha='right')
    
# plt.title('서울 자치구별 반려동물 등록수와 미세먼지 농도 산점도', fontsize=16)
# plt.xlabel('반려동물 등록수', fontsize=10)
# plt.ylabel('미세먼지 농도 (연평균)', fontsize=12)
# plt.xticks(rotation=45, ha='right', fontsize=8)  # 폰트 크기 축소
# plt.yticks(fontsize=10)
# plt.grid(axis='y')
# plt.tight_layout()
# # 이미지 저장
# output_path = 'RESULT/visualization/등록수_VS_미세먼지_포함_scatter.png'
# os.makedirs(os.path.dirname(output_path), exist_ok=True)
# plt.savefig(output_path, dpi=300, bbox_inches='tight')
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sklearn.preprocessing import MinMaxScaler
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

df=df_merge

print(df.columns)
import numpy as np  # 꼭 있어야 함





# 정규화
scaler = MinMaxScaler()
df[['반려동물 등록수_norm', '미세먼지 농도_norm']] = scaler.fit_transform(df[['반려동물 등록수', '미세먼지 농도']])

# 회귀선 기울기 계산 (정규화된 데이터 사용)
slope, intercept = np.polyfit(df['반려동물 등록수_norm'], df['미세먼지 농도_norm'], 1)
print(f"정규화된 회귀선 기울기: {slope:.4f}, 절편: {intercept:.4f}")

# 시각화
plt.figure(figsize=(12, 9))

# 산점도
sns.scatterplot(data=df, x='반려동물 등록수_norm', y='미세먼지 농도_norm', color='skyblue', label='자치구')

# 회귀선
sns.regplot(data=df, x='반려동물 등록수_norm', y='미세먼지 농도_norm',
            scatter=False, color='black', line_kws={"linestyle": "dashed"}, label='회귀선')

# 라벨 추가
for i in range(df.shape[0]):
    plt.text(x=df.loc[i, '반려동물 등록수_norm'] + 0.005,
             y=df.loc[i, '미세먼지 농도_norm'],
             s=df.loc[i, '자치구'],
             fontsize=8)

plt.title('정규화된 반려동물 등록수 vs 미세먼지 농도', fontsize=14)
plt.xlabel('정규화된 반려동물 등록수', fontsize=12)
plt.ylabel('정규화된 "미세먼지 농도"', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# 이미지 저장
output_path = '/home/jiming/dev_ws/eda-repo-3/RESULT/visualization/정규화/정규화_CO원.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
