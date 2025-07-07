
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# # ▶️ .env 파일의 환경변수 불러오기
# load_dotenv()
# host = os.getenv("DB_HOST")
# user = os.getenv("DB_USER")
# password = os.getenv("DB_PASSWORD")
# database = os.getenv("DB_NAME")

# # ▶️ MySQL 연결
# engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# # ▶️ 데이터 조회
# query = """
# SELECT 
#     sido as 시도,
#     sigungu as 시군구,
#     dog_registered_total as 개등록_누계,
#     cat_registered_total as 고양이등록_누계,
#     total_registered as 총등록_누계
# FROM companion_animal_registration
# WHERE sido = '서울특별시'
# ORDER BY total_registered DESC
# """
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/home/qatest/eda/eda-repo-3/RESULT/csv/seoul_integrated_data.csv")

# 필요한 컬럼만 선택
selected_df = df[[
                  'companion_animal_registration', 
                  'seoul_noise_vibration_complaint', 
                  'pollution_co_concentration_by_station', 
                  'pollution_emission_facility']]

# 상관관계 분석
correlation_matrix = selected_df.corr()

# 시각화: 상관관계 히트맵
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("환경/사회 지표 간 상관관계 분석")
plt.tight_layout()
plt.show()

correlation_matrix

