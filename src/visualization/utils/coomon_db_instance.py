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


def select_common_db(query: str)-> pd.DataFrame:

    # ▒ .env 환경변수 로드
    load_dotenv()
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    # ▒ DB 연결
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

    if not query:
    # ▒ 데이터 조회
        query = """
    SELECT 
        district_level_2 AS 자치구,
        noise_vibration_complaint AS '소음·진동 민원',
        factory_noise_vibration_complaint AS '공장 소음·진동',
        traffic_noise_vibration_complaint AS '교통 소음·진동',
        life_noise_vibration_complaint AS '생활 소음·진동'
    FROM seoul_noise_vibration_complaint
    WHERE district_level_2 != '합계'
    """
    df = pd.read_sql(query, engine)

    return df

# select_common_db(engine)