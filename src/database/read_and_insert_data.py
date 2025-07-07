import pandas as pd
from utils.db_functions import get_connection, execute_sql, close_conn_and_cursor
from utils.pd_to_db_functions import pd_to_db
from sqlalchemy import create_engine

from dotenv import load_dotenv
import os

# .env 파일을 찾아 환경 변수로 로드
load_dotenv()

# 환경 변수 가져오기
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# table = 'seoul_animal_hospital'
# raw_file_path = 'DATA/서울시 동물병원 인허가 정보.csv'

# table = 'companion_animal_registration'
# raw_file_path = 'DATA/Number of registered companion animals by administrative district_20221231.csv'

# table = 'animal_hospital_registry'
# raw_file_path = 'DATA/행정안전부_동물병원_20240302.csv'

table = 'pollution_pm25_concentration_by_station'
raw_file_path = 'DATA/[도시대기측정망]측정소별 초미세먼지 농도 측정결과(2023년).csv'


print(f"DB 접속 정보: {host=} {user=} {password=} {database=}")

db_connection, cursor = pd_to_db(host, user, password, database, table, raw_file_path)

close_conn_and_cursor(db_connection, cursor)


