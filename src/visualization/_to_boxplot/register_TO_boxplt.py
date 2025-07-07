import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# ▶️ .env 파일의 환경변수 불러오기
load_dotenv("env")
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▶️ MySQL 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# ▶️ 데이터 조회
query = """
SELECT 
    sigungu as 시군구,
    total_registered as 총등록_누계
FROM companion_animal_registration
WHERE sido = '서울특별시'
ORDER BY total_registered DESC
"""
df = pd.read_sql(query, engine)

df.columns = ['시군구','총등록_누계']

print(df)



# scatter ==========================================

plt.figure(figsize=(8, 12))
plt.boxplot(df['총등록_누계'])

# 개별 값들 y 좌표로 찍기 (x 좌표는 1로 고정)
x = [1] * len(df)
y = df['총등록_누계']

plt.scatter(x, y, color='red')

# 각 점에 시군구 이름 라벨 붙이기
for i, txt in enumerate(df['시군구']):
    plt.text(1.05, y[i], txt, fontsize=8)

plt.title('시군구별 총등록_누계 분포와 위치')
plt.ylabel('총등록_누계')
plt.grid(True)




# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/반려동물등록_boxplot.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()