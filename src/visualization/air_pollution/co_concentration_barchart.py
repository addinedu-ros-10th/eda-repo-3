import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
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

# 데이터 조회: 서울특별시의 자치구별 월별 CO 농도
query = """
SELECT 
    city AS 자치구,
    january, february, march, april, may, june, 
    july, august, september, october, november, december
FROM pollution_co_concentration_by_station
WHERE province = '서울특별시'
"""

df = pd.read_sql(query, engine)

# 월별 long format으로 변환
df_melted = df.melt(id_vars='자치구', 
                    value_vars=['january', 'february', 'march', 'april', 'may', 'june',
                                'july', 'august', 'september', 'october', 'november', 'december'],
                    var_name='월', value_name='CO농도(ppm)')

# 월 영문 → 한글 매핑
month_mapping = {
    'january': '1월', 'february': '2월', 'march': '3월', 'april': '4월',
    'may': '5월', 'june': '6월', 'july': '7월', 'august': '8월',
    'september': '9월', 'october': '10월', 'november': '11월', 'december': '12월'
}
df_melted['월'] = df_melted['월'].map(month_mapping)

# 자치구 이름 기준 정렬
df_melted = df_melted.sort_values(by='자치구')

# 시각화
plt.figure(figsize=(18, 8))
sns.barplot(data=df_melted, x='자치구', y='CO농도(ppm)', hue='월')

plt.title('서울 자치구별 월별 CO 농도 (ppm)', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.legend(title='월', bbox_to_anchor=(1.01, 1), loc='upper left')
plt.tight_layout()
plt.show()