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
# SELECT station_name, annual_avg
# FROM pollution_co_concentration_by_station
# WHERE province = '서울'
# """
# query2 = """
# SELECT * FROM pollution_co_concentration_by_station
# """

# df = pd.read_sql(query1, engine)
# df.rename(columns={'station_name' : '자치구',
#                    'annual_avg' : 'CO 농도'},
#           inplace=True)
# df

# df_sorted = df.sort_values('CO 농도', ascending=False)


# # ▶️ csv 불러오기 경로 지정
# input_path = os.path.join('RESULT','csv','seoul_integrated_data.csv')
# # input_path = 'RESULT/csv/seoul_integrated_data.csv'
# # os.path.dirname(output_path)
# df = pd.read_csv(input_path)
# df

# # 1. 복사 명시
# df_companion = df.iloc[:, [0,1]].copy()
# df_companion.rename(columns={
#   'district' : '자치구',
#   'companion_animal_registration' : '반려동물 등록수'}, inplace=True)

# # 2. 병합
# df_merge = pd.merge(df_companion, df_sorted, on='자치구', how='outer')

# # 3. 산점도 그리기
# plt.figure(figsize=(10,6))
# plt.scatter(df_merge['반려동물 등록수'], df_merge['CO 농도'], color='blue', alpha=0.7, edgecolors='black')

# plt.xlabel('반려동물 등록수')
# plt.ylabel('CO 농도 (ppm)')
# plt.title('자치구별 반려동물 등록수와 CO 농도 산점도')
# plt.grid(True)
# plt.tight_layout()
# # 이미지 저장
# output_path = 'RESULT/visualization/등록수_VS_COOO_scatter.png'
# os.makedirs(os.path.dirname(output_path), exist_ok=True)
# plt.savefig(output_path, dpi=300, bbox_inches='tight')
# plt.show()


# ============================================================================
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import platform
from sklearn.preprocessing import MinMaxScaler
import numpy as np

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
SELECT station_name, annual_avg
FROM pollution_co_concentration_by_station
WHERE province = '서울'
"""
df = pd.read_sql(query1, engine)
df.rename(columns={'station_name' : '자치구',
                   'annual_avg' : 'CO 농도'}, inplace=True)

df_sorted = df.sort_values('CO 농도', ascending=False)

# csv 불러오기
input_path = os.path.join('RESULT','csv','seoul_integrated_data.csv')
df_reg = pd.read_csv(input_path)

df_companion = df_reg.iloc[:, [0,1]].copy()
df_companion.rename(columns={
  'district' : '자치구',
  'companion_animal_registration' : '반려동물 등록수'}, inplace=True)

df_merge = pd.merge(df_companion, df_sorted, on='자치구', how='outer')

df = df_merge
print(df.columns)

# 정규화
scaler = MinMaxScaler()
df[['반려동물 등록수_norm', 'CO 농도_norm']] = scaler.fit_transform(df[['반려동물 등록수', 'CO 농도']])

# 회귀선 기울기 계산 (정규화된 데이터 사용)
slope, intercept = np.polyfit(df['반려동물 등록수_norm'], df['CO 농도_norm'], 1)
print(f"정규화된 회귀선 기울기: {slope:.4f}, 절편: {intercept:.4f}")

# 시각화
plt.figure(figsize=(12, 9))

# 산점도
sns.scatterplot(data=df, x='반려동물 등록수_norm', y='CO 농도_norm', color='skyblue', label='자치구')

# 회귀선
sns.regplot(data=df, x='반려동물 등록수_norm', y='CO 농도_norm',
            scatter=False, color='black', line_kws={"linestyle": "dashed"}, label='회귀선')

# 라벨 추가
for i in range(df.shape[0]):
    plt.text(x=df.loc[i, '반려동물 등록수_norm'] + 0.005,
             y=df.loc[i, 'CO 농도_norm'],
             s=df.loc[i, '자치구'],
             fontsize=8)

plt.title('정규화된 반려동물 등록수 vs CO 농도', fontsize=14)
plt.xlabel('정규화된 반려동물 등록수', fontsize=12)
plt.ylabel('정규화된 "CO 농도"', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# 이미지 저장
output_path = '/home/jiming/dev_ws/eda-repo-3/RESULT/visualization/정규화/정규화_CO원.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
