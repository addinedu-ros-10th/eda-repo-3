import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# # ▶️ 한글 폰트 설정
# plt.rcParams['font.family'] = 'AppleGothic'
# plt.rcParams['axes.unicode_minus'] = False

# ▶️ 환경변수 로드 및 DB 연결
load_dotenv()
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# ▶️ SQL 쿼리 (%%로 수정!)
query = """
SELECT 
	animal_registration.gu '자치구',
    animal_registration.cnt '반려동물등록수',
    # park_area.total_area_sqm '1인당 공원면적',
	animal_beauty.cnt '미용업소 수',
	animal_facility.cnt '위탁시설 수',
	animal_hospital.cnt '동물병원 수'
FROM
(SELECT 
	sigungu gu,
    total_registered cnt
FROM companion_animal_registration
WHERE sido = '서울특별시') animal_registration,
(SELECT
	district_category_2 gu,
    COALESCE(per_capita_park_area_sqm ,0) +
    COALESCE(per_capita_urban_park_area_sqm ,0) AS total_area_sqm
FROM eda.per_capita_park_area
WHERE district_category_2 not in ('소계', '서울대공원')
) park_area,
(SELECT
	COALESCE(
        REGEXP_SUBSTR(address_jibun, '[^ ]+구'),
        REGEXP_SUBSTR(road_address, '[^ ]+구')
    ) AS gu,
    COUNT(*) AS cnt
FROM animal_beauty_business
WHERE 
(address_jibun LIKE '%%서울%%'
OR road_address LIKE '%%서울%%')
AND (
REGEXP_SUBSTR(address_jibun, '[^ ]+구') NOT IN ('남동구','단원구', '부평구','해운대구')
OR REGEXP_SUBSTR(road_address, '[^ ]+구') NOT IN ('남동구','단원구', '부평구','해운대구')
)
GROUP BY gu) animal_beauty,
(SELECT
    COALESCE(
        REGEXP_SUBSTR(jibun_address, '[^ ]+구'),
        REGEXP_SUBSTR(road_address, '[^ ]+구')
    ) AS gu,
    COUNT(*) AS cnt
FROM eda.seoul_animal_trust_facility
WHERE road_address LIKE '%%서울%%'
   OR jibun_address LIKE '%%서울%%'
GROUP BY gu
HAVING gu IS NOT NULL
) animal_facility,
(SELECT gu, cnt
FROM (SELECT
 COALESCE(
        REGEXP_SUBSTR(jibun_address, '[^ ]+구'),
        REGEXP_SUBSTR(road_address, '[^ ]+구')
    ) AS gu,
    COUNT(*) AS cnt
FROM animal_hospital_registry
WHERE 
(jibun_address LIKE '%%서울%%'
OR road_address LIKE '%%서울%%')
GROUP BY gu) a
WHERE
(gu not in ('서울대학교그린바이오과학기술연구','철산상업지구','분당구','단원구','소사구') AND gu != '')) animal_hospital
WHERE 
animal_registration.gu = park_area.gu
AND animal_registration.gu = animal_beauty.gu
AND animal_registration.gu = animal_facility.gu
AND animal_registration.gu = animal_hospital.gu
ORDER BY 반려동물등록수 DESC
# LIMIT 10
"""

# ▶️ 데이터프레임 생성
df = pd.read_sql(query, engine)

# ▶️ 정규화(Min-Max Scaling) 처리
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df.drop(columns="자치구"))
df_scaled = pd.DataFrame(scaled, columns=df.columns[1:])
df_scaled["자치구"] = df["자치구"]
df_scaled = df_scaled.set_index("자치구").sort_values("반려동물등록수", ascending=False)

# ▶️ 시각화: 다중 막대 그래프
# plt.figure(figsize=(18, 9))
df_scaled.plot(kind="bar", figsize=(18, 9), width=0.85)
plt.title("서울 자치구별 반려동물 관련 지표 비교 (정규화 스케일)")
plt.ylabel("정규화 값 (0~1)")
plt.xlabel("자치구")
plt.xticks(rotation=45)
plt.legend(loc="upper right")
plt.tight_layout()
plt.grid(axis='y')

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/서울_자치구별_반려동물_관련_지표_비교_(정규화 스케일).png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()
