import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

import platform
if platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
elif platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

load_dotenv('env')
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

query = """
SELECT 
    city AS 자치구,
    january, february, march, april, may, june, 
    july, august, september, october, november, december
FROM pollution_co_concentration_by_station
WHERE province = '서울특별시'
"""

df = pd.read_sql(query, engine)

register_df = pd.DataFrame({
    'district': ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구',
                 '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구',
                 '용산구', '은평구', '종로구', '중구', '중랑구'],
    'total_registered': [34843, 25515, 18585, 33636, 26408, 20272, 19412, 12925, 27138, 19873,
                         19074, 18509, 23441, 17781, 23786, 16889, 24200, 33706, 23770, 18997,
                         17760, 28005, 9577, 8042, 23018]
})

# long format 변환
df_melted = df.melt(id_vars='자치구', 
                    value_vars=['january', 'february', 'march', 'april', 'may', 'june',
                                'july', 'august', 'september', 'october', 'november', 'december'],
                    var_name='월', value_name='CO농도(ppm)')

month_mapping = {
    'january': '1월', 'february': '2월', 'march': '3월', 'april': '4월',
    'may': '5월', 'june': '6월', 'july': '7월', 'august': '8월',
    'september': '9월', 'october': '10월', 'november': '11월', 'december': '12월'
}
df_melted['월'] = df_melted['월'].map(month_mapping)

# 자치구명 기준으로 register_df와 병합
df_merged = pd.merge(df_melted, register_df, left_on='자치구', right_on='district')
print(df_merged)
import numpy as np  # 꼭 있어야 함

# 회귀선 기울기 및 절편 계산
slope, intercept = np.polyfit(df_merged['total_registered'], df_merged['CO농도(ppm)'], 1)
print(f"회귀선 기울기: {slope:.6f}, 절편: {intercept:.4f}")


plt.title('반려동물 등록수 vs 서울 자치구별 월별 CO 농도', fontsize=16)
plt.xlabel('반려동물 등록수')
plt.ylabel('CO 농도 (ppm)')
plt.grid(True)
plt.legend(title='월', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# 이미지 저장
output_path = 'RESULT/visualization/등록수_VS_CO_scatter.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')


plt.show()
