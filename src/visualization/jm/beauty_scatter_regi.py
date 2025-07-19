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

# df=pd.read_csv('/home/jiming/dev_ws/eda-repo-3/RESULT/csv/seoul_integrated_data.csv')

# # 동물 시설 관련 column만 사용하기
# df_filterd = df.iloc[:, :7]
# df_filterd.drop(columns=['companion_animal_registration'], inplace=True)
# df_filterd.drop(columns=['seoul_animal_hospital'],inplace=True)
# print(df_filterd)



# #=============



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

df = pd.merge(facility_df, register_df, on='district')

# 위탁업체 수 기준으로 상위/하위 5개 추출
top5 = df.nlargest(5, 'animal_trust_count')
bottom5 = df.nsmallest(5, 'animal_trust_count')
middle = df[~df['district'].isin(top5['district']) & ~df['district'].isin(bottom5['district'])]

# 시각화
plt.figure(figsize=(12, 9))

# 중간 그룹 (회색)
sns.scatterplot(data=middle, x='total_registered', y='animal_trust_count', label='기타 지역', color='gray')

# 상위 5개 (파란색)
sns.scatterplot(data=top5, x='total_registered', y='animal_trust_count', label='위탁업체 수 상위 5개', color='blue')

# 하위 5개 (빨간색)
sns.scatterplot(data=bottom5, x='total_registered', y='animal_trust_count', label='위탁업체 수 하위 5개', color='red')

# 회귀선 (신뢰구간 포함)
sns.regplot(data=df, x='total_registered', y='animal_trust_count',
            scatter=False, color='black', line_kws={"linestyle": "dashed"}, label='회귀선')

# 라벨 추가
for i in range(df.shape[0]):
    plt.text(x=df.loc[i, 'total_registered'] + 300,
             y=df.loc[i, 'animal_trust_count'],
             s=df.loc[i, 'district'],
             fontsize=8)

# 제목 및 축
plt.title('반려동물 등록수 vs 위탁업체 수', fontsize=14)
plt.xlabel('반려동물 등록수', fontsize=12)
plt.ylabel('위탁업체 수', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# 이미지 저장
output_path = 'RESULT/visualization/등록수_VS_위탁업체수_scatter.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')

plt.show()



# df['total_facility'] = df[['hospital_count', 'beauty_count', 'pharmacy_count', 'animal_trust_count']].sum(axis=1)

# print(df)
# # 5) total_count vs total_registered 산점도 + 라벨 표시 ==============================
# plt.figure(figsize=(10,8))
# sns.scatterplot(data=df, x='total_facility', y='total_registered')

# for i in range(df.shape[0]):
#     plt.text(x=df.loc[i, 'total_facility'] + 0.5,
#              y=df.loc[i, 'total_registered'],
#              s=df.loc[i, 'district'],
#              fontsize=8)

# plt.title('총 반려시설 수 vs 반려동물 등록수')
# plt.xlabel('총 반려시설 수')
# plt.ylabel('반려동물 등록수')
# plt.grid(True)

# # ▶️ 이미지 저장 경로 지정
# output_path = 'RESULT/visualization/총반려시설수_VS_등록수_scatter.png'
# os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
# plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

# plt.show()