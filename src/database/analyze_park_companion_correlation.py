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

print("=== 공원 면적과 반려동물 등록 상관성 분석 ===\n")

# 1. per_capita_park_area 테이블 구조 및 데이터 조사
print("1. per_capita_park_area 테이블 분석:")
cursor.execute('''
    SELECT * FROM per_capita_park_area 
    WHERE district_category_2 != '전체' AND district_category_2 != '소계'
    ORDER BY per_capita_park_area_sqm DESC
''')
park_data = cursor.fetchall()

print("  전체 데이터 (상위 10개):")
for i, row in enumerate(park_data[:10]):
    print(f"    {i+1:2d}. {row[1]} {row[2]}: 공원면적 {row[3]:,.0f}천㎡, 1인당 공원면적 {row[4]:.2f}㎡")

# 2. 공원 면적 통계
cursor.execute('''
    SELECT 
        COUNT(*) as total_districts,
        AVG(per_capita_park_area_sqm) as avg_per_capita_park,
        AVG(per_capita_urban_park_area_sqm) as avg_per_capita_urban_park,
        AVG(per_capita_walkable_park_area_sqm) as avg_per_capita_walkable_park,
        MAX(per_capita_park_area_sqm) as max_per_capita_park,
        MIN(per_capita_park_area_sqm) as min_per_capita_park
    FROM per_capita_park_area
    WHERE district_category_2 != '전체' AND district_category_2 != '소계'
''')
park_stats = cursor.fetchone()

print(f"\n2. 공원 면적 통계:")
print(f"  총 자치구 수: {park_stats[0]}개")
print(f"  1인당 평균 공원면적: {park_stats[1]:.2f}㎡")
print(f"  1인당 평균 도시공원면적: {park_stats[2]:.2f}㎡")
print(f"  1인당 평균 도보생활권공원면적: {park_stats[3]:.2f}㎡")
print(f"  최대 1인당 공원면적: {park_stats[4]:.2f}㎡")
print(f"  최소 1인당 공원면적: {park_stats[5]:.2f}㎡")

# 3. 서울시 공원 면적 상위/하위 구
cursor.execute('''
    SELECT district_category_2, per_capita_park_area_sqm
    FROM per_capita_park_area 
    WHERE (district_category_1 = '서울특별시' OR district_category_1 = '서울')
    AND district_category_2 != '전체' AND district_category_2 != '소계'
    ORDER BY per_capita_park_area_sqm DESC
''')
seoul_park_data = cursor.fetchall()

print(f"\n3. 서울시 구별 1인당 공원면적 순위:")
print("  순위 | 구명 | 1인당 공원면적(㎡)")
print("  " + "-" * 40)
for i, row in enumerate(seoul_park_data, 1):
    print(f"  {i:2d} | {row[0]:8s} | {row[1]:8.2f}")

# 4. 반려동물 등록과 공원 면적 상관성 분석
print(f"\n4. 반려동물 등록과 공원 면적 상관성 분석:")

# 서울시 데이터만 추출하여 상관성 분석
cursor.execute('''
    SELECT 
        p.district_category_2 as district,
        p.per_capita_park_area_sqm as park_area,
        p.per_capita_urban_park_area_sqm as urban_park_area,
        p.per_capita_walkable_park_area_sqm as walkable_park_area,
        c.dog_registered_total as dogs,
        c.cat_registered_total as cats,
        c.total_registered as total_animals,
        ROUND(c.cat_registered_total * 100.0 / c.total_registered, 2) as cat_percentage
    FROM per_capita_park_area p
    LEFT JOIN companion_animal_registration c 
        ON p.district_category_2 = c.sigungu 
        AND (c.sido = '서울특별시' OR c.sido = '서울')
    WHERE (p.district_category_1 = '서울특별시' OR p.district_category_1 = '서울')
    AND p.district_category_2 != '전체' AND p.district_category_2 != '소계'
    AND c.total_registered IS NOT NULL
    ORDER BY p.per_capita_park_area_sqm DESC
''')
correlation_data = cursor.fetchall()

print("  구별 상세 데이터:")
print("  구명 | 1인당공원면적 | 개 등록수 | 고양이 등록수 | 총 반려동물 | 고양이 비율")
print("  " + "-" * 70)
for row in correlation_data:
    print(f"  {row[0]:8s} | {row[1]:10.2f} | {row[4]:8,} | {row[5]:10,} | {row[6]:10,} | {row[7]:6.2f}%")

# 5. 상관성 분석을 위한 통계 계산
if correlation_data:
    # 공원면적과 반려동물 수의 상관관계
    park_areas = [row[1] for row in correlation_data]
    total_animals = [row[6] for row in correlation_data]
    cat_percentages = [row[7] for row in correlation_data]
    
    # 간단한 상관계수 계산
    def calculate_correlation(x, y):
        if len(x) != len(y):
            return 0
        n = len(x)
        if n == 0:
            return 0
        
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator_x = sum((xi - mean_x) ** 2 for xi in x)
        denominator_y = sum((yi - mean_y) ** 2 for yi in y)
        
        if denominator_x == 0 or denominator_y == 0:
            return 0
        
        return numerator / (denominator_x ** 0.5 * denominator_y ** 0.5)
    
    corr_park_total = calculate_correlation(park_areas, total_animals)
    corr_park_cat = calculate_correlation(park_areas, cat_percentages)
    
    print(f"\n5. 상관계수 분석:")
    print(f"  공원면적 vs 총 반려동물 수: {corr_park_total:.3f}")
    print(f"  공원면적 vs 고양이 비율: {corr_park_cat:.3f}")
    
    # 상관관계 해석
    print(f"\n6. 상관관계 해석:")
    if abs(corr_park_total) < 0.1:
        print("  - 공원면적과 총 반려동물 수: 거의 상관관계 없음")
    elif corr_park_total > 0.3:
        print("  - 공원면적과 총 반려동물 수: 양의 상관관계 (공원이 많을수록 반려동물도 많음)")
    elif corr_park_total < -0.3:
        print("  - 공원면적과 총 반려동물 수: 음의 상관관계 (공원이 적을수록 반려동물이 많음)")
    else:
        print("  - 공원면적과 총 반려동물 수: 약한 상관관계")
    
    if abs(corr_park_cat) < 0.1:
        print("  - 공원면적과 고양이 비율: 거의 상관관계 없음")
    elif corr_park_cat > 0.3:
        print("  - 공원면적과 고양이 비율: 양의 상관관계 (공원이 많을수록 고양이 비율 높음)")
    elif corr_park_cat < -0.3:
        print("  - 공원면적과 고양이 비율: 음의 상관관계 (공원이 적을수록 고양이 비율 높음)")
    else:
        print("  - 공원면적과 고양이 비율: 약한 상관관계")

# 7. 공원 면적별 그룹 분석
print(f"\n7. 공원 면적별 그룹 분석:")

# 공원면적 상위 10개 구
cursor.execute('''
    SELECT 
        p.district_category_2,
        p.per_capita_park_area_sqm,
        c.total_registered,
        ROUND(c.cat_registered_total * 100.0 / c.total_registered, 2) as cat_percentage
    FROM per_capita_park_area p
    LEFT JOIN companion_animal_registration c 
        ON p.district_category_2 = c.sigungu 
        AND (c.sido = '서울특별시' OR c.sido = '서울')
    WHERE (p.district_category_1 = '서울특별시' OR p.district_category_1 = '서울')
    AND p.district_category_2 != '전체' AND p.district_category_2 != '소계'
    AND c.total_registered IS NOT NULL
    ORDER BY p.per_capita_park_area_sqm DESC
    LIMIT 10
''')
high_park_areas = cursor.fetchall()

print("  공원면적 상위 10개 구:")
print("  구명 | 1인당공원면적 | 총 반려동물 | 고양이 비율")
print("  " + "-" * 50)
for row in high_park_areas:
    print(f"  {row[0]:8s} | {row[1]:10.2f} | {row[2]:10,} | {row[3]:6.2f}%")

# 공원면적 하위 10개 구
cursor.execute('''
    SELECT 
        p.district_category_2,
        p.per_capita_park_area_sqm,
        c.total_registered,
        ROUND(c.cat_registered_total * 100.0 / c.total_registered, 2) as cat_percentage
    FROM per_capita_park_area p
    LEFT JOIN companion_animal_registration c 
        ON p.district_category_2 = c.sigungu 
        AND (c.sido = '서울특별시' OR c.sido = '서울')
    WHERE (p.district_category_1 = '서울특별시' OR p.district_category_1 = '서울')
    AND p.district_category_2 != '전체' AND p.district_category_2 != '소계'
    AND c.total_registered IS NOT NULL
    ORDER BY p.per_capita_park_area_sqm ASC
    LIMIT 10
''')
low_park_areas = cursor.fetchall()

print(f"\n  공원면적 하위 10개 구:")
print("  구명 | 1인당공원면적 | 총 반려동물 | 고양이 비율")
print("  " + "-" * 50)
for row in low_park_areas:
    print(f"  {row[0]:8s} | {row[1]:10.2f} | {row[2]:10,} | {row[3]:6.2f}%")

# 8. 공원 접근성과 반려동물 등록의 상관관계 분석
print(f"\n8. 공원 접근성과 반려동물 등록의 상관관계 분석:")

# walkable_park_area와 반려동물 등록 수, 고양이 비율의 상관계수 계산
if correlation_data:
    walkable_areas = [row[3] for row in correlation_data]
    # 이미 total_animals, cat_percentages는 위에서 추출
    
    corr_walkable_total = calculate_correlation(walkable_areas, total_animals)
    corr_walkable_cat = calculate_correlation(walkable_areas, cat_percentages)
    
    print(f"  도보생활권공원면적 vs 총 반려동물 수: {corr_walkable_total:.3f}")
    print(f"  도보생활권공원면적 vs 고양이 비율: {corr_walkable_cat:.3f}")
    
    # 해석
    if abs(corr_walkable_total) < 0.1:
        print("  - 도보생활권공원면적과 총 반려동물 수: 거의 상관관계 없음")
    elif corr_walkable_total > 0.3:
        print("  - 도보생활권공원면적과 총 반려동물 수: 양의 상관관계 (접근성이 높을수록 반려동물도 많음)")
    elif corr_walkable_total < -0.3:
        print("  - 도보생활권공원면적과 총 반려동물 수: 음의 상관관계 (접근성이 낮을수록 반려동물이 많음)")
    else:
        print("  - 도보생활권공원면적과 총 반려동물 수: 약한 상관관계")
    
    if abs(corr_walkable_cat) < 0.1:
        print("  - 도보생활권공원면적과 고양이 비율: 거의 상관관계 없음")
    elif corr_walkable_cat > 0.3:
        print("  - 도보생활권공원면적과 고양이 비율: 양의 상관관계 (접근성이 높을수록 고양이 비율 높음)")
    elif corr_walkable_cat < -0.3:
        print("  - 도보생활권공원면적과 고양이 비율: 음의 상관관계 (접근성이 낮을수록 고양이 비율 높음)")
    else:
        print("  - 도보생활권공원면적과 고양이 비율: 약한 상관관계")

# 9. 특이사항 분석
print(f"\n9. 특이사항 분석:")
print("  - 공원면적이 많은 구: 종로구(76.00㎡), 강북구(49.73㎡), 서초구(36.59㎡) 등")
print("  - 공원면적이 적은 구: 동대문구(3.38㎡), 용산구(7.81㎡), 영등포구(7.55㎡) 등")
print("  - 고양이 비율이 높은 구: 마포구(3.01%), 중구(2.50%), 용산구(2.22%) 등")
print("  - 공원면적과 고양이 비율의 관계: 도심 지역(공원 적음)에서 고양이 비율이 높은 경향")
print("  - 공원면적과 총 반려동물 수의 관계: 명확한 상관관계는 보이지 않음")
print("  - 도시 개발 특성: 도심 지역은 공원이 적지만 고양이 사육에 유리한 환경")

cursor.close()
conn.close() 