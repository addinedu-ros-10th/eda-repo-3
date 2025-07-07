import pandas as pd
from functools import reduce
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sqlalchemy import create_engine
from shapely.geometry import shape
from io import BytesIO
import base64

from dotenv import load_dotenv
import os
import json

# .env 파일을 찾아 환경 변수로 로드
load_dotenv()

# 환경 변수 가져오기
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▶️ MySQL 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

'''
data1 : 농림축산식품부 농림축산검역본부_행정구역별 반려동물등록 개체 수 현황
data2 : 서울시 동물병원 인허가 정보
data3 : 행정안전부_동물병원
data4 : 행정안전부_동물 미용업
data5 : 행정안전부_동물약국
data6 : 행정안전부_동물위탁관리업
data7 : 전국도시공원정보표준데이터
data8 : 서울특별시_유기동물보호 현황 통계 (자치구별)
data9 : 기후환경본부_소음진동민원 현황
data10 : 에어코리아_월별 미세먼지농도(2023)
data11 : 서울시 환경오염물질 배출시설
data12 : [보고서] 2016-2020 유실·유기동물 분석 보고서
data13 : 공원(1인당+공원면적)

column1 : (자치구당) 반려동물등록 개체 수
column2 : (자치구당) 동물병원 수
column3 : (자치구당 행정안전부) 동물병원 수
column4 : (자치구별) 동물 미용업 수
column5 : (자치구별) 동물약국 수
column6 : (자치구별) 동물위탁관리업 수
column7 : (자치구별) 공원 수
column8 : (자치구별) 유기동물 수
column9 : (자치구별) 안락사동물 수
column10 : (자치구별) 소음진동민원 수
column11 : (자치구별) CO농도
column12 : (자치구별) 환경오염물질 배출시설 수
column13 : 2016-2020 서울시 유기동물 발생 평균값
column14 : 1인당 공원 면적
column15 : 1인당 도시공원 면적
column16 : 1인당 도보생활권 공원면적
'''

# 1. companion_animal_registration 테이블
  # 농림축산식품부 농림축산검역본부_행정구역별 반려동물등록 개체 수 현황
  # return coluum
    # district : 구 이름
    # companion_animal_registration : (자치구당) 반려동물등록 개체 수
def get_companion_animal_registration():
  #     sido as 시도,
  # ▶️ 데이터 조회
  query = """
  SELECT 
      sigungu as district,
      total_registered as companion_animal_registration
  FROM companion_animal_registration
  WHERE sido = '서울특별시'
  ORDER BY total_registered DESC
  """
  df = pd.read_sql(query, engine)

  return df


# 2. seoul_animal_hospital 테이블
  # 서울시 동물병원 인허가 정보
  # return coluum
    # district : 구 이름
    # seoul_animal_hospital : (자치구당) 동물병원 수
def get_seoul_animal_hospital():
  # ▒ 데이터 조회
  query = """
  SELECT road_address, jibun_address
  FROM seoul_animal_hospital
  WHERE status_name in ('영업/정상')  -- 폐업 제외
  """
  df = pd.read_sql(query, engine)


  # ▒ 자치구 추출 함수
  def extract_district(address):
      # match = re.search(r'서울\s*(\S+구)', str(address))
      # return match.group(1) if match else None
      if address:
          return address.split(' ')[1]
      else:
          None

  # ▒ 자치구 컬럼 생성
  df['district'] = df['road_address'].apply(extract_district)
  df['district'] = df['district'].fillna(df['jibun_address'].apply(extract_district))

  # print(df)

  # ▒ 병원 수 집계
  district_count = df['district'].value_counts().reset_index()
  district_count.columns = ['district', 'seoul_animal_hospital']
  district_count = district_count.sort_values(by='seoul_animal_hospital', ascending=False)

  return district_count


# 3. animal_hospital_registry 테이블
  # 행정안전부_동물병원
  # return coluum
    # district : 구 이름
    # seoul_animal_hospital : (자치구당 행정안전부) 동물병원 수
def get_animal_hospital_registry():
  query = """
  SELECT jibun_address
  FROM animal_hospital_registry
  WHERE (status_name LIKE '영업/정상') AND (jibun_address LIKE '서울특별시%%')
  """
  df = pd.read_sql(query, engine)

  # 구 이름 추출 방법 1: 문자열 분할
  df['district'] = df['jibun_address'].str.split(' ').str[2]

  # 구 이름 추출 방법 2: 정규표현식 사용
  import re
  df['district'] = df['jibun_address'].str.extract(r'서울특별시 ([가-힣]+구)')

  # 구별 개수 집계
  district_counts = df['district'].value_counts().reset_index()
  district_counts.columns = ['district', 'hospital_count']
  district_counts = district_counts.sort_values('hospital_count', ascending=False)

  return district_counts


# 4. animal_beauty_business 테이블
  # 행정안전부_동물 미용업
  # return coluum
    # district : 구 이름
    # beauty_count : (자치구별) 동물 미용업 수
def get_animal_beauty_business():
  query = """
  SELECT *
  FROM animal_beauty_business
  WHERE (status_name LIKE '영업/정상') AND (address_jibun LIKE '서울특별시%%')
  """
  df = pd.read_sql(query, engine)

  # 구 이름 추출 방법 1: 문자열 분할
  df['district'] = df['address_jibun'].str.split(' ').str[2]

  # 구 이름 추출 방법 2: 정규표현식 사용
  import re
  df['district'] = df['address_jibun'].str.extract(r'서울특별시 ([가-힣]+구)')

  # 구별 개수 집계
  district_counts = df['district'].value_counts().reset_index()
  district_counts.columns = ['district', 'beauty_count']
  district_counts = district_counts.sort_values('beauty_count', ascending=False)

  return district_counts

# 5. animal_pharmacy_registry 테이블
  # 행정안전부_동물약국
  # return coluum
    # district : 구 이름
    # pharmacy_count : (자치구별) 동물약국 수
def get_animal_pharmacy_registry():
  query = """
  SELECT *
  FROM animal_pharmacy_registry
  WHERE (status_name LIKE '영업/정상') AND (jibun_address LIKE '서울특별시%%')
  """
  df = pd.read_sql(query, engine)

  # 구 이름 추출 방법 1: 문자열 분할
  df['district'] = df['jibun_address'].str.split(' ').str[2]

  # 구 이름 추출 방법 2: 정규표현식 사용
  import re
  df['district'] = df['jibun_address'].str.extract(r'서울특별시 ([가-힣]+구)')

  # 구별 개수 집계
  district_counts = df['district'].value_counts().reset_index()
  district_counts.columns = ['district', 'pharmacy_count']
  district_counts = district_counts.sort_values('pharmacy_count', ascending=False)

  return district_counts

# 6. seoul_animal_trust_facility 테이블
  # 행정안전부_동물위탁관리업
  # return coluum
    # district : 구 이름
    # animal_trust_count : (자치구별) 동물위탁관리업 수
def get_seoul_animal_trust_facility():
  query = """
  SELECT *
  FROM seoul_animal_trust_facility
  WHERE (status_name LIKE '영업/정상') AND (jibun_address LIKE '서울특별시%%')
  """
  df = pd.read_sql(query, engine)

  # 구 이름 추출 방법 1: 문자열 분할
  df['district'] = df['jibun_address'].str.split(' ').str[2]

  # 구 이름 추출 방법 2: 정규표현식 사용
  import re
  df['district'] = df['jibun_address'].str.extract(r'서울특별시 ([가-힣]+구)')

  # 구별 개수 집계
  district_counts = df['district'].value_counts().reset_index()
  district_counts.columns = ['district', 'animal_trust_count']
  district_counts = district_counts.sort_values('animal_trust_count', ascending=False)

  return district_counts

# 7. korea_urban_park_info 테이블
  # 전국도시공원정보표준데이터
  # return coluum
    # district : 구 이름
    # korea_urban_park_info : (자치구별) 공원 수
def get_korea_urban_park_info():
  query = """
  SELECT jibun_address as 주소, latitude as 위도, longitude as 경도, park_area as 면적, provider_name as 제공처
  FROM korea_urban_park_info
  WHERE jibun_address like "%%서울%%"
  """
  df = pd.read_sql(query, engine)

  df.columns =['주소', '위도', '경도', '면적', '제공처']

  # 자치구별로 구분하기
  df['district'] = df['제공처'].str.extract(r'서울특별시\s+(\S+구)')


  df_grouped = df.groupby('district').size().reset_index(name ='count')

  df_sorted = df_grouped.sort_values(by='count', ascending=False)
  df_sorted.columns = ['district', 'korea_urban_park_info']
  return df_sorted

# 8. seoul_abandoned_animal_status 테이블
  # 서울특별시_유기동물보호 현황 통계 (자치구별)
  # return coluum
    # district : 구 이름
    # abandon_count : (자치구별) 유기동물 수
    # deceased_count : (자치구별) 안락사동물 수
def get_seoul_abandoned_animal_status():
  # ▶️ seoul_abandoned_animal_status 등록 데이터 가져오기
  query = """
  SELECT district_level_2 AS district, 
        dog_total, cat_total, dog_deceased, cat_deceased
  FROM seoul_abandoned_animal_status
  """
  df = pd.read_sql(query, engine)
  # 개 / 고양이 유기동물 발생 합계 계산
  # 개 / 고양이 안락사 발생 합계 계산

  # 0번행(총계) 제거
  df.drop(0, inplace=True)

  # 구별 개수 집계
  df['abandon_count'] = df['dog_total'] + df['cat_total']
  df['deceased_count'] = df['dog_deceased'] + df['cat_deceased']

  # 필요한 컬럼만 추출
  result_df = df[['district', 'abandon_count', 'deceased_count']]
  return result_df

# 9. seoul_noise_vibration_complaint 테이블
  # 기후환경본부_소음진동민원 현황
  # return coluum
    # district : 구 이름
    # seoul_noise_vibration_complaint : (자치구별) 소음진동민원 수
def get_seoul_noise_vibration_complaint():
    # ▒ 데이터 조회
    query = """
    SELECT 
        district_level_2 AS district,
        noise_vibration_complaint AS '소음·진동 민원',
        factory_noise_vibration_complaint AS '공장 소음·진동',
        traffic_noise_vibration_complaint AS '교통 소음·진동',
        life_noise_vibration_complaint AS '생활 소음·진동'
    FROM seoul_noise_vibration_complaint
    WHERE district_level_2 != '소계'
    """
    df = pd.read_sql(query, engine)

    # ▒ 자치구별 총 민원 수 기준 내림차순 정렬
    df['seoul_noise_vibration_complaint'] = df[['공장 소음·진동', '교통 소음·진동', '생활 소음·진동']].sum(axis=1)
    df = df.sort_values(by='seoul_noise_vibration_complaint', ascending=False)

    df_result = df[['district', 'seoul_noise_vibration_complaint']]
    return df_result

# 10. pollution_co_concentration_by_station 테이블
  # 에어코리아_월별 미세먼지농도(2023)
  # return coluum
    # district : 구 이름
    # pollution_co_concentration_by_station : (자치구별) CO농도
def get_pollution_co_concentration_by_station():
    query = """
    SELECT 
        station_name AS district,
        january, february, march, april, may, june, 
        july, august, september, october, november, december
    FROM pollution_co_concentration_by_station
    WHERE province = '서울'
    """

    df = pd.read_sql(query, engine)

    # 월별 long format으로 변환
    df_melted = df.melt(id_vars='district', 
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
    df_melted = df_melted.sort_values(by='district')

    # 월별 long format 데이터(300행)를 자치구별 집계 데이터(25행)로 변환

    # 기존 월별 데이터 (df_melted)
    # df_melted: 자치구, 월, CO농도(ppm) 컬럼을 가진 300행 데이터프레임

    # 자치구별 CO농도 집계 (평균 계산)
    df_district_summary = df_melted.groupby('district')['CO농도(ppm)'].mean().reset_index()
    df_district_summary.columns = ['district', 'pollution_co_concentration_by_station']

    # 평균값 반올림 (소수점 3자리)
    df_district_summary['pollution_co_concentration_by_station'] = df_district_summary['pollution_co_concentration_by_station'].round(3)

    # 자치구 이름 기준 정렬
    df_district_summary = df_district_summary.sort_values(by='district')

    # 인덱스 초기화
    df_district_summary = df_district_summary.reset_index(drop=True)

    return df_district_summary

# 11. pollution_emission_facility 테이블
  # 서울시 환경오염물질 배출시설
  # return coluum
    # district : 구 이름
    # pollution_emission_facility : (자치구별) 환경오염물질 배출시설 수
def get_pollution_emission_facility():
	# ▒ 데이터 조회
	query = """
	SELECT 
		*
	FROM pollution_emission_facility
	WHERE region_small != '소계'
	"""
	df = pd.read_sql(query, engine)

	# 시각화용 정제 및 정렬
	df_chart = df[["region_small"]].copy()
	df_chart.rename(columns={'region_small' : 'district'}, inplace=True)
	df_chart['pollution_emission_facility'] = df["air_total"] + df["water_total"] + df["noise_total"]

	# df_chart = df_chart.sort_values(by=["air_total", "water_total", "noise_total"], ascending=False)

	df_chart = df_chart.sort_values(by=['pollution_emission_facility'], ascending=False)
	return df_chart

# 12. seoul_abandonment_statistics 테이블
  # [보고서] 2016-2020 유실·유기동물 분석 보고서
  # return coluum
    # district : 구 이름
    # seoul_abandonment_statistics : 2016-2020 서울시 유기동물 발생 평균값
def get_seoul_abandonment_statistics():
  # ▶️ 유기동물 마리수 가져오기
  query = """
  SELECT *
  FROM seoul_abandonment_statistics
  ORDER BY district_name
  """
  df = pd.read_sql(query, engine)
  df.columns =['id','자치구', '2016', '2017', '2018', '2019', '2020', '삭제']

  # 필요없는 column 제거하기
  df = df.drop(columns =['id', '삭제'])

  # 평균값 구하기
  df['seoul_abandonment_statistics'] = df[['2016', '2017', '2018', '2019', '2020']].mean(axis=1)

  df_sorted = df.sort_values(by='seoul_abandonment_statistics', ascending=False)
  df_sorted.rename(columns={'자치구' : 'district'},inplace=True)
  df_sorted = df_sorted[['district', 'seoul_abandonment_statistics']]

  return df_sorted

# 13. per_capita_park_area 테이블
  # 공원(1인당+공원면적)
  # return coluum
    # district : 구 이름
    # 1인당 공원 면적
    # 1인당 도시공원 면적
    # 1인당 도보생활권 공원면적
def get_per_capita_park_area():
  # ▶️ 유기동물 마리수 가져오기
  query = """
  SELECT district_category_2, per_capita_park_area_sqm, per_capita_urban_park_area_sqm, per_capita_walkable_park_area_sqm
  FROM per_capita_park_area
  WHERE district_category_2  not like "서울대공원"
  ORDER BY district_category_2;
  """
  df = pd.read_sql(query, engine)
  df.columns =['district', '1인당 공원 면적', '1인당 도시공원 면적', '1인당 도보생활권 공원면적']

  return df


def create_integrated_dataframe_and_save_csv():
    """13개 함수의 결과를 통합하여 하나의 DataFrame을 생성하고 CSV로 저장"""
    
    # 각 함수 호출하여 DataFrame 리스트 생성
    dfs = [
        get_companion_animal_registration(),   # ①
        get_seoul_animal_hospital(),           # ②
        get_animal_hospital_registry(),        # ③
        get_animal_beauty_business(),          # ④
        get_animal_pharmacy_registry(),        # ⑤
        get_seoul_animal_trust_facility(),     # ⑥
        get_korea_urban_park_info(),           # ⑦
        get_seoul_abandoned_animal_status(),   # ⑧
        get_seoul_noise_vibration_complaint(), # ⑨
        get_pollution_co_concentration_by_station(), # ⑩
        get_pollution_emission_facility(),     # ⑪
        get_seoul_abandonment_statistics(),    # ⑫
        get_per_capita_park_area()             # ⑬
    ]
    
    # district를 기준으로 순차 병합 (outer join)
    merged_df = reduce(lambda left, right: pd.merge(left, right, on='district', how='outer'), dfs)
    
    # district 열을 첫 번째로 고정 & 알파벳(가나다) 순 정렬
    cols = ['district'] + [c for c in merged_df.columns if c != 'district']
    merged_df = merged_df[cols].sort_values('district').reset_index(drop=True)
    merged_df = merged_df[merged_df['district'] != '소계']


    # CSV 파일로 저장
    merged_df.to_csv('~/eda-repo-3/RESULT/csv/seoul_integrated_data.csv', index=False, encoding='utf-8-sig')
    
    print("✅ 통합 DataFrame이 'seoul_integrated_data.csv'로 저장되었습니다.")
    print(f"📊 데이터 형태: {merged_df.shape} (행, 열)")
    print(f"📝 컬럼 목록: {list(merged_df.columns)}")
    
    return merged_df

if __name__=='__main__':
  create_integrated_dataframe_and_save_csv()
