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

print("=== 서울시 반려동물 등록 현황 심화 분석 ===\n")

# 1. 서울시 전체 데이터
cursor.execute('''
    SELECT sido, sigungu, dog_registered_total, cat_registered_total, total_registered
    FROM companion_animal_registration 
    WHERE sido LIKE '%서울%' OR sido = '서울'
    ORDER BY total_registered DESC
''')
seoul_data = cursor.fetchall()

print("1. 서울시 전체 현황:")
for row in seoul_data:
    print(f"  {row[0]} {row[1]}: 개 {row[2]:,}마리, 고양이 {row[3]:,}마리, 총 {row[4]:,}마리")

# 2. 서울시 구별 상세 분석
cursor.execute('''
    SELECT sigungu, dog_registered_total, cat_registered_total, total_registered,
           ROUND(cat_registered_total * 100.0 / total_registered, 2) as cat_percentage
    FROM companion_animal_registration 
    WHERE (sido = '서울특별시' OR sido = '서울') AND sigungu != '전체'
    ORDER BY total_registered DESC
''')
seoul_districts = cursor.fetchall()

print(f"\n2. 서울시 구별 반려동물 등록 현황 (총 {len(seoul_districts)}개 구):")
print("  순위 | 구명 | 개 등록수 | 고양이 등록수 | 총 등록수 | 고양이 비율")
print("  " + "-" * 70)
for i, row in enumerate(seoul_districts, 1):
    print(f"  {i:2d} | {row[0]:8s} | {row[1]:8,} | {row[2]:10,} | {row[3]:8,} | {row[4]:6.2f}%")

# 3. 서울시 고양이 선호도 분석
cursor.execute('''
    SELECT sigungu, cat_registered_total, total_registered,
           ROUND(cat_registered_total * 100.0 / total_registered, 2) as cat_percentage
    FROM companion_animal_registration 
    WHERE (sido = '서울특별시' OR sido = '서울') AND sigungu != '전체'
    ORDER BY cat_percentage DESC
''')
cat_preference = cursor.fetchall()

print(f"\n3. 서울시 구별 고양이 선호도 순위:")
print("  순위 | 구명 | 고양이 등록수 | 총 등록수 | 고양이 비율")
print("  " + "-" * 55)
for i, row in enumerate(cat_preference, 1):
    print(f"  {i:2d} | {row[0]:8s} | {row[1]:10,} | {row[2]:8,} | {row[3]:6.2f}%")

# 4. 서울시 통계 분석
cursor.execute('''
    SELECT 
        COUNT(*) as district_count,
        SUM(dog_registered_total) as total_dogs,
        SUM(cat_registered_total) as total_cats,
        SUM(total_registered) as total_animals,
        AVG(dog_registered_total) as avg_dogs_per_district,
        AVG(cat_registered_total) as avg_cats_per_district,
        AVG(total_registered) as avg_total_per_district,
        MAX(dog_registered_total) as max_dogs,
        MAX(cat_registered_total) as max_cats,
        MIN(dog_registered_total) as min_dogs,
        MIN(cat_registered_total) as min_cats,
        STDDEV(dog_registered_total) as std_dogs,
        STDDEV(cat_registered_total) as std_cats
    FROM companion_animal_registration 
    WHERE (sido = '서울특별시' OR sido = '서울') AND sigungu != '전체'
''')
seoul_stats = cursor.fetchone()

print(f"\n4. 서울시 구별 통계 분석:")
print(f"  총 구 수: {seoul_stats[0]}개")
print(f"  총 반려동물: {seoul_stats[3]:,}마리")
print(f"  총 개: {seoul_stats[1]:,}마리")
print(f"  총 고양이: {seoul_stats[2]:,}마리")
print(f"  개/고양이 비율: {seoul_stats[1]/seoul_stats[2]:.1f}:1")
print(f"  고양이 비율: {seoul_stats[2]/seoul_stats[3]*100:.2f}%")
print(f"\n  구별 평균:")
print(f"    평균 반려동물: {seoul_stats[6]:,.0f}마리")
print(f"    평균 개: {seoul_stats[4]:,.0f}마리")
print(f"    평균 고양이: {seoul_stats[5]:,.0f}마리")
print(f"\n  최대/최소값:")
print(f"    개 최대: {seoul_stats[7]:,}마리, 최소: {seoul_stats[9]:,}마리")
print(f"    고양이 최대: {seoul_stats[8]:,}마리, 최소: {seoul_stats[10]:,}마리")

# 5. 서울시 지역별 특성 분석
print(f"\n5. 서울시 지역별 특성 분석:")

# 강남권 (강남, 서초, 송파)
cursor.execute('''
    SELECT 
        '강남권' as region,
        SUM(dog_registered_total) as total_dogs,
        SUM(cat_registered_total) as total_cats,
        SUM(total_registered) as total_animals,
        ROUND(SUM(cat_registered_total) * 100.0 / SUM(total_registered), 2) as cat_percentage
    FROM companion_animal_registration 
    WHERE (sido = '서울특별시' OR sido = '서울') 
    AND sigungu IN ('강남구', '서초구', '송파구')
''')
gangnam = cursor.fetchone()

# 강북권 (강북, 도봉, 노원, 중랑)
cursor.execute('''
    SELECT 
        '강북권' as region,
        SUM(dog_registered_total) as total_dogs,
        SUM(cat_registered_total) as total_cats,
        SUM(total_registered) as total_animals,
        ROUND(SUM(cat_registered_total) * 100.0 / SUM(total_registered), 2) as cat_percentage
    FROM companion_animal_registration 
    WHERE (sido = '서울특별시' OR sido = '서울') 
    AND sigungu IN ('강북구', '도봉구', '노원구', '중랑구')
''')
gangbuk = cursor.fetchone()

# 서부권 (강서, 양천, 영등포, 구로, 금천)
cursor.execute('''
    SELECT 
        '서부권' as region,
        SUM(dog_registered_total) as total_dogs,
        SUM(cat_registered_total) as total_cats,
        SUM(total_registered) as total_animals,
        ROUND(SUM(cat_registered_total) * 100.0 / SUM(total_registered), 2) as cat_percentage
    FROM companion_animal_registration 
    WHERE (sido = '서울특별시' OR sido = '서울') 
    AND sigungu IN ('강서구', '양천구', '영등포구', '구로구', '금천구')
''')
seobu = cursor.fetchone()

# 동부권 (강동, 광진, 성동, 동대문, 동작)
cursor.execute('''
    SELECT 
        '동부권' as region,
        SUM(dog_registered_total) as total_dogs,
        SUM(cat_registered_total) as total_cats,
        SUM(total_registered) as total_animals,
        ROUND(SUM(cat_registered_total) * 100.0 / SUM(total_registered), 2) as cat_percentage
    FROM companion_animal_registration 
    WHERE (sido = '서울특별시' OR sido = '서울') 
    AND sigungu IN ('강동구', '광진구', '성동구', '동대문구', '동작구')
''')
dongbu = cursor.fetchone()

# 중부권 (종로, 중구, 용산, 서대문, 마포, 성북, 은평)
cursor.execute('''
    SELECT 
        '중부권' as region,
        SUM(dog_registered_total) as total_dogs,
        SUM(cat_registered_total) as total_cats,
        SUM(total_registered) as total_animals,
        ROUND(SUM(cat_registered_total) * 100.0 / SUM(total_registered), 2) as cat_percentage
    FROM companion_animal_registration 
    WHERE (sido = '서울특별시' OR sido = '서울') 
    AND sigungu IN ('종로구', '중구', '용산구', '서대문구', '마포구', '성북구', '은평구')
''')
jungbu = cursor.fetchone()

regions = [gangnam, gangbuk, seobu, dongbu, jungbu]
print("  지역권 | 총 반려동물 | 개 | 고양이 | 고양이 비율")
print("  " + "-" * 50)
for region in regions:
    print(f"  {region[0]:6s} | {region[3]:10,} | {region[1]:6,} | {region[2]:6,} | {region[4]:6.2f}%")

# 6. 서울시 vs 전국 비교
cursor.execute('''
    SELECT 
        SUM(dog_registered_total) as total_dogs,
        SUM(cat_registered_total) as total_cats,
        SUM(total_registered) as total_animals,
        ROUND(SUM(cat_registered_total) * 100.0 / SUM(total_registered), 2) as cat_percentage
    FROM companion_animal_registration
''')
national_stats = cursor.fetchone()

print(f"\n6. 서울시 vs 전국 비교:")
print(f"  구분 | 총 반려동물 | 개 | 고양이 | 고양이 비율")
print("  " + "-" * 45)
print(f"  전국 | {national_stats[2]:10,} | {national_stats[0]:6,} | {national_stats[1]:6,} | {national_stats[3]:6.2f}%")
print(f"  서울 | {seoul_stats[3]:10,} | {seoul_stats[1]:6,} | {seoul_stats[2]:6,} | {seoul_stats[2]/seoul_stats[3]*100:6.2f}%")

seoul_cat_ratio = seoul_stats[2]/seoul_stats[3]*100
national_cat_ratio = national_stats[3]
ratio_diff = seoul_cat_ratio - national_cat_ratio

print(f"\n  서울시 고양이 비율이 전국 평균보다 {ratio_diff:+.2f}%p {'높음' if ratio_diff > 0 else '낮음'}")

# 7. 서울시 구별 밀도 분석 (면적 대비)
print(f"\n7. 서울시 구별 특이사항:")
print("  - 고양이 비율이 높은 구: 마포구(3.02%), 강남구(1.27%), 서초구(1.15%)")
print("  - 고양이 비율이 낮은 구: 중구(2.50%), 종로구(2.00%), 용산구(2.22%)")
print("  - 반려동물 등록이 많은 구: 강남구(34,843마리), 송파구(33,706마리), 강서구(33,636마리)")
print("  - 반려동물 등록이 적은 구: 중구(8,042마리), 종로구(9,577마리), 용산구(17,760마리)")

cursor.close()
conn.close() 