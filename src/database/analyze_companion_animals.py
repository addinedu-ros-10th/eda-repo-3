import os
from dotenv import load_dotenv
from src.database.utils.db_functions import get_connection_and_cursor
import pandas as pd

load_dotenv('env')
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')

conn, cursor = get_connection_and_cursor(host, user, password, database)

print("=== companion_animal_registration 테이블 분석 ===\n")

# 1. 전체 데이터 조회
cursor.execute('SELECT * FROM companion_animal_registration ORDER BY total_registered DESC')
data = cursor.fetchall()
print("1. 전체 데이터:")
for row in data:
    print(f"  {row}")

# 2. 기본 통계
cursor.execute('SELECT COUNT(*) FROM companion_animal_registration')
total_records = cursor.fetchone()[0]
print(f"\n2. 총 레코드 수: {total_records}")

# 3. 시도별 분석
cursor.execute('''
    SELECT sido, 
           COUNT(*) as region_count,
           SUM(dog_registered_total) as total_dogs,
           SUM(cat_registered_total) as total_cats,
           SUM(total_registered) as total_animals,
           AVG(dog_registered_total) as avg_dogs,
           AVG(cat_registered_total) as avg_cats,
           AVG(total_registered) as avg_total
    FROM companion_animal_registration 
    GROUP BY sido 
    ORDER BY total_animals DESC
''')
sido_stats = cursor.fetchall()
print("\n3. 시도별 분석:")
for row in sido_stats:
    print(f"  {row[0]}: 총 {row[4]}마리 (개: {row[2]}, 고양이: {row[3]})")

# 4. 개 vs 고양이 비율
cursor.execute('''
    SELECT 
        SUM(dog_registered_total) as total_dogs,
        SUM(cat_registered_total) as total_cats,
        SUM(total_registered) as total_animals,
        ROUND(SUM(dog_registered_total) * 100.0 / SUM(total_registered), 2) as dog_percentage,
        ROUND(SUM(cat_registered_total) * 100.0 / SUM(total_registered), 2) as cat_percentage
    FROM companion_animal_registration
''')
ratio_stats = cursor.fetchone()
print(f"\n4. 개 vs 고양이 비율:")
print(f"  총 반려동물: {ratio_stats[2]:,}마리")
print(f"  개: {ratio_stats[0]:,}마리 ({ratio_stats[3]}%)")
print(f"  고양이: {ratio_stats[1]:,}마리 ({ratio_stats[4]}%)")

# 5. 상위/하위 지역
cursor.execute('''
    SELECT sido, sigungu, total_registered 
    FROM companion_animal_registration 
    ORDER BY total_registered DESC 
    LIMIT 5
''')
top_regions = cursor.fetchall()
print(f"\n5. 반려동물 등록 수 상위 5개 지역:")
for i, row in enumerate(top_regions, 1):
    print(f"  {i}. {row[0]} {row[1]}: {row[2]:,}마리")

cursor.execute('''
    SELECT sido, sigungu, total_registered 
    FROM companion_animal_registration 
    WHERE total_registered > 0
    ORDER BY total_registered ASC 
    LIMIT 5
''')
bottom_regions = cursor.fetchall()
print(f"\n6. 반려동물 등록 수 하위 5개 지역:")
for i, row in enumerate(bottom_regions, 1):
    print(f"  {i}. {row[0]} {row[1]}: {row[2]:,}마리")

# 6. 지역별 개/고양이 선호도
cursor.execute('''
    SELECT sido, sigungu,
           CASE 
               WHEN dog_registered_total > cat_registered_total THEN '개 선호'
               WHEN cat_registered_total > dog_registered_total THEN '고양이 선호'
               ELSE '동일'
           END as preference,
           dog_registered_total,
           cat_registered_total,
           total_registered
    FROM companion_animal_registration
    ORDER BY total_registered DESC
''')
preferences = cursor.fetchall()
print(f"\n7. 지역별 개/고양이 선호도:")
dog_prefer = sum(1 for row in preferences if row[2] == '개 선호')
cat_prefer = sum(1 for row in preferences if row[2] == '고양이 선호')
same_prefer = sum(1 for row in preferences if row[2] == '동일')
print(f"  개 선호 지역: {dog_prefer}개")
print(f"  고양이 선호 지역: {cat_prefer}개")
print(f"  동일한 지역: {same_prefer}개")

# 7. 상세 선호도 분석
print(f"\n8. 상위 10개 지역의 선호도:")
for i, row in enumerate(preferences[:10], 1):
    print(f"  {i}. {row[0]} {row[1]}: {row[2]} (개: {row[3]:,}, 고양이: {row[4]:,}, 총: {row[5]:,})")

cursor.close()
conn.close() 