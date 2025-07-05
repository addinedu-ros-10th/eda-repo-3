import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import folium
from sqlalchemy import create_engine
from shapely.geometry import shape
from io import BytesIO
import base64
import seaborn as sns

from dotenv import load_dotenv
import os
import json

df=pd.read_csv('/home/seojimin/dev_ws/eda-repo-3/RESULT/csv/seoul_integrated_data.csv')

# 동물 시설 관련 column만 사용하기
df_filterd = df.iloc[:, :7]
df_filterd.drop(columns=['companion_animal_registration'], inplace=True)
df_filterd.drop(columns=['seoul_animal_hospital'],inplace=True)
print(df_filterd)



#=============


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# # 예시 facility 데이터 (위 데이터)
facility_df = pd.DataFrame({
    'district': ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구',
                 '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구',
                 '용산구', '은평구', '종로구', '중구', '중랑구'],
    'hospital_count': [94, 47, 27, 50, 27, 33, 29, 16, 45, 26, 32, 21, 47, 27, 53, 26, 34, 83, 49, 37, 28, 42, 12, 19, 31],
    'beauty_count': [154, 87, 56, 101, 57, 56, 45, 40, 83, 59, 57, 43, 61, 50, 85, 50, 74, 143, 68, 59, 41, 77, 13, 19, 70],
    'pharmacy_count': [287, 156, 69, 146, 118, 89, 92, 62, 117, 73, 92, 67, 115, 78, 158, 66, 87, 180, 83, 116, 32, 125, 81, 57, 88],
    'animal_trust_count': [102, 37, 28, 60, 34, 22, 13, 24, 24, 21, 30, 16, 27, 20, 41, 20, 23, 88, 32, 28, 32, 27, 6, 11, 29]
})

# 예시 반려동물 등록수 데이터
register_df = pd.DataFrame({
    'district': ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구',
                 '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구',
                 '용산구', '은평구', '종로구', '중구', '중랑구'],
    'total_registered': [34843, 25515, 18585, 33636, 26408, 20272, 19412, 12925, 27138, 19873,
                         19074, 18509, 23441, 17781, 23786, 16889, 24200, 33706, 23770, 18997,
                         17760, 28005, 9577, 8042, 23018]
})

# 두 데이터 병합 (district 기준)
df = pd.merge(facility_df, register_df, on='district')

# 1) hospital_count vs total_registered 산점도 + 라벨 표시 =======================================
plt.figure(figsize=(10,8))
sns.scatterplot(data=df, x='hospital_count', y='total_registered')

# 각 점에 district 이름 표시
for i in range(df.shape[0]):
    plt.text(x=df.loc[i, 'hospital_count'] + 0.5,  # +0.5는 글자가 점과 겹치지 않게 약간 띄움
             y=df.loc[i, 'total_registered'],
             s=df.loc[i, 'district'],
             fontsize=8)

plt.title('병원 수 vs 반려동물 등록수')
plt.xlabel('병원 수')
plt.ylabel('반려동물 등록수')
plt.grid(True)


# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/병원수_VS_등록수_scatter.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()


# 2) beauty_count vs total_registered 산점도 + 라벨 표시 ============================
plt.figure(figsize=(10,8))
sns.scatterplot(data=df, x='beauty_count', y='total_registered')

for i in range(df.shape[0]):
    plt.text(x=df.loc[i, 'beauty_count'] + 0.5,
             y=df.loc[i, 'total_registered'],
             s=df.loc[i, 'district'],
             fontsize=8)

plt.title('미용업체 수 vs 반려동물 등록수')
plt.xlabel('미용업체 수')
plt.ylabel('반려동물 등록수')
plt.grid(True)

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/미용업체수_VS_등록수_scatter.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()

# 3) pharmacy_count vs total_registered 산점도 + 라벨 표시 ===================================
plt.figure(figsize=(10,8))
sns.scatterplot(data=df, x='pharmacy_count', y='total_registered')

for i in range(df.shape[0]):
    plt.text(x=df.loc[i, 'pharmacy_count'] + 0.5,
             y=df.loc[i, 'total_registered'],
             s=df.loc[i, 'district'],
             fontsize=8)

plt.title('약국 수 vs 반려동물 등록수')
plt.xlabel('약국 수')
plt.ylabel('반려동물 등록수')
plt.grid(True)

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/약국수_VS_등록수_scatter.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()

# 4) animal_trust_count vs total_registered 산점도 + 라벨 표시 ==============================
plt.figure(figsize=(10,8))
sns.scatterplot(data=df, x='animal_trust_count', y='total_registered')

for i in range(df.shape[0]):
    plt.text(x=df.loc[i, 'animal_trust_count'] + 0.5,
             y=df.loc[i, 'total_registered'],
             s=df.loc[i, 'district'],
             fontsize=8)

plt.title('위탁업체 수 vs 반려동물 등록수')
plt.xlabel('위탁업체 수')
plt.ylabel('반려동물 등록수')
plt.grid(True)

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/위탁업체수_VS_등록수_scatter.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()


