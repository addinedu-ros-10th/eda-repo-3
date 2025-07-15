# 동물병원 인허가 정보 (서울시)

* 테이블 구조: [seoul_animal_hospital](#seoul_animal_hospital)

<br/>

* 목적:

    서울시 공공데이터에서 제공하는 동물병원 인허가 정보를 저장합니다.
    인허가 일자, 폐업/휴업 상태, 병원 위치, 좌표, 업종 구분 등 상세한 행정 데이터를 포함합니다.

<br/>

* 주요 필드:

    * licensg_de, status_name, jibun_address, x, y, 등 총 31개 필드

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 반려동물 관련 의료 인프라 분석

    * GIS 기반 병원 위치 시각화

    * 서울시 각 구역별 동물병원 운영 현황 분석

# 행정구역별 반려동물 등록 현황 (농림축산식품부)

* 테이블 구조: [companion_animal_registration](#companion_animal_registration)

<br/>

* 목적:

    행정구역별 반려동물 등록 현황(개/고양이/전체)을 저장합니다.
    등록 수 기준으로 지역별 반려동물 분포를 파악할 수 있도록 구성되어 있습니다.

<br/>

* 주요 필드:

    * sido: 시도명

    * sigungu: 시군구명

    * dog_registered_total, cat_registered_total, total_registered: 누적 등록 수

<br/>

* 활용 예시:

    * 반려동물 등록률 지도 시각화

    * 지역별 반려동물 복지 정책 수립 자료

    * 동물병원 분포 대비 수요 분석

# 동물병원 등록 정보 (행정안전부)

* 테이블 구조: [animal_hospital_registry](#animal_hospital_registry)

<br/>

* 목적:

    행정안전부에서 제공하는 동물병원 등록 정보를 체계적으로 저장하기 위한 테이블입니다.
    기초 주소 정보, 병원명, 전화번호, 인허가 상태, 업종 정보, 위치 좌표 등 공공 행정데이터를 포함합니다.

<br/>

* 주요 필드:

    * licensg_de, status_name, jibun_address, x, y 등 총 33개 필드

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 반려동물 관련 의료 인프라 분석

    * GIS 기반 병원 위치 시각화

    * 병원 인허가 상태 및 운영 현황 분석

# 동물미용업 인허가 정보 (행정안전부)

* 테이블 구조: [animal_beauty_business](#animal_beauty_business)

<br/>

* 목적:

    행정안전부가 제공하는 동물미용업 관련 인허가 정보를 저장합니다.
    인허가 상태, 소재지 정보, 좌표 정보, 영업 구분 및 갱신 정보 등 다양한 행정 데이터 포함.

<br/>

* 주요 필드:

    * licensg_de, status_name, road_address, x, y 등 총 32개 필드

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 반려동물 산업 현황 분석

    * 미용업소 분포 기반 상권 분석

    * 미용 관련 민원 및 인허가 대응 분석 등


# 동물약국 인허가 정보 (행정안전부)

* 테이블 구조: [animal_pharmacy_registry](#animal_pharmacy_registry)

<br/>

* 목적:

    행정안전부에서 제공하는 동물약국 인허가 정보를 저장합니다.
    병원 상태, 위치, 전화번호, 주소, 인허가 일자 등 행정 데이터를 정리하여 향후 분석과 활용이 가능하게 합니다.

<br/>

* 주요 필드:

    * licensg_de, status_name, jibun_address, x, y 등 포함 총 32개 필드

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 지역별 동물약국 분포 분석

    * 인허가 추이 분석

    * GIS 좌표 기반 시각화

# 동물위탁관리업 인허가 정보 (서울시)

* 테이블 구조: [seoul_animal_trust_facility](#seoul_animal_trust_facility)

<br/>

* 목적:
    서울시 공공데이터에서 제공하는 동물위탁관리업 인허가 정보를 저장합니다.
    전화번호, 주소, 사업장명, 영업상태, 좌표, 업무 구분 등 상세한 행정 데이터를 포함합니다.

<br/>

* 주요 필드:

    * licensg_de, status_name, road_address, x, y 등 총 33개 필드

    * created_at: 데이터 적재 일시 자동 기록
<br/>

* 활용 예시:

    * 위탁 반려동물 관리 인프라 파악

    * 서울시 지역별 동물 위탁시설 분포 분석

    * 위치 기반 서비스(GIS) 활용

# 전국 도시공원 정보 표준 데이터 (행정안전부)

* 테이블 구조: [korea_urban_park_info](#korea_urban_park_info)

<br/>

* 목적:

    전국의 도시공원 정보를 표준화하여 관리하기 위한 테이블입니다. 공원명, 위치, 보유 시설, 면적, 관리기관 등 다양한 정보를 포함하여 지역 인프라 분석 및 정책 수립에 활용됩니다.

<br/>

* 주요 필드:

    * park_name: 공원명

    * latitude, longitude: 공원 위치 좌표

    * park_area: 공원 면적

    * facility_*: 공원 내 보유 시설 정보

    * managing_agency, phone_number: 관리 기관 정보

    * designated_date: 공원 지정일자

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 도시 인프라 분포 및 접근성 분석

    * 반려동물 산책 가능한 공간 정보 분석

    * 지역별 공공 편의시설 현황 시각화



# 서울특별시 유기동물보호 현황 통계 (행정안전부)

* 테이블 구조: [seoul_abandoned_animal_status](#seoul_abandoned_animal_status)

<br/>

* 목적:

    서울시 각 자치구별 유기동물 보호 및 처리 현황 정보를 저장합니다.
    보호된 유기동물의 종류별 처리 방식(주인 인도, 입양, 폐사 등)을 분석하는 데 사용됩니다.

<br/>

* 주요 필드:

    * district_level_1, district_level_2: 행정 구역

    * total_count: 전체 유기동물 수

    * 각 동물종(개, 고양이, 기타)에 대한 처리 방식별 소계

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 자치구별 유기동물 구조 및 처리 건수 통계 분석

    * 반려동물 정책 수립을 위한 기초 데이터 활용

    * 유기동물 보호소 운영 효율화 및 입양 캠페인 기획

# 서울시 소음진동민원 현황 통계 (서울시)

* 테이블 구조: [seoul_noise_vibration_complaint](#seoul_noise_vibration_complaint)

<br/>

* 목적:

    서울시 각 자치구별 소음 및 진동 관련 민원 데이터를 저장합니다. 공장, 교통, 생활 소음 등으로 분류된 데이터를 통해 도시 소음 환경의 문제점을 파악하고 지역별 정책 수립 및 대응 전략 수립에 활용합니다.

<br/>

* 주요 필드:

    * district_level_1, district_level_2: 행정 구역

    * noise_vibration_complaint: 총 소음진동 민원 수

    * factory_noise_vibration_complaint, traffic_noise_vibration_complaint, life_noise_vibration_complaint: 원인별 분류

<br/>

* 활용 예시:

    * 지역별 소음 민원 집중도 분석

    * 소음 유발 요인별 정책 대응

    * GIS 시각화를 통한 소음 민원 분포도 제작

# 환경오염물질 배출시설 통계 (서울시)

* 테이블 구조: [pollution_emission_facility](#pollution_emission_facility)

<br/>

* 목적:

    2024년 기준 지역별 환경오염물질(대기, 수질, 소음·진동) 배출시설의 분포 및 분류 정보를 저장합니다. 대기오염, 폐수, 소음·진동 항목을 각 1~5종으로 세분화하여 관리하며, 지역별 이중 분류 체계를 통해 정온지역 여부를 포함한 환경 영향을 분석할 수 있습니다.

<br/>

* 주요 필드:

    * region_large, region_small

    * air_total, air_type_1~5

    * water_total, water_type_1~5

    * noise_total, noise_silent_area, noise_non_silent_area

<br/>

* 활용 예시:

    * 지역별 환경오염 시설 밀도 분석

    * 정온지역 소음 관리 대상 지역 파악

    * 오염물질 종류 및 등급에 따른 규제 수립

# 서울특별시 자치구별 유기동물 발생 통계 (동물 자유 연대)

* 테이블 구조: [seoul_abandonment_statistics](#seoul_abandonment_statistics)

<br/>

* 목적:

    서울특별시 자치구별 유기동물 발생 건수를 연도별로 기록하여 유기동물 발생 추세를 시계열로 분석할 수 있도록 합니다. 2016년부터 2020년까지의 데이터가 포함되어 있으며, 각 자치구별 유기 발생 현황을 데이터 기반으로 파악할 수 있습니다.

<br/>

* 주요 필드:

    * district_name: 자치구 이름 (예: 강남구, 종로구 등)

    * abandonment_count_2016~2020: 각 연도별 유기동물 발생 건수

    * created_at: 데이터 적재 일시 (자동 기록)

<br/>

* 활용 예시:

    * 서울시 유기동물 발생 추세 시각화 (연도별 증가/감소 비교)

    * 자치구별 유기동물 발생률 비교를 통한 정책 우선순위 설정

    * 동물 보호소 수요 예측 및 자원 배분 기준자료 제공


# 서울특별시 자치구별 공원면적 및 도시공원·생활권공원 면적 정보 (서울시)

* 테이블 구조: [per_capita_park_area](#per_capita_park_area)
<br/>

* 목적:

    서울시 각 자치구별 1인당 공원면적 및 도시공원·생활권공원 관련 면적 정보를 저장합니다.
    이는 도시 녹지 환경 및 생활 인프라 분석에 활용됩니다.

<br/>

* 주요 필드:

    * district_category_1, district_category_2: 자치구 분류

    * park_area_total_sqm_thousands, per_capita_park_area_sqm: 전체 공원 면적 및 1인당 공원 면적 

    * urban_park_area_sqm_thousands, per_capita_urban_park_area_sqm: 도시공원 관련 정보

    * walkable_park_area_sqm_thousands, per_capita_walkable_park_area_sqm: 도보생활권공원 관련 정보

<br/>

* created_at: 데이터 적재 일시 자동 기록

    * 활용 예시:

    * 자치구별 녹지공간 불균형 분석

    * 환경복지 및 보행권 분석

    * 도시개발 정책 우선순위 판단 근거


# 전국 도시대기측정망 2023년 일산화탄소(CO) 농도 측정 결과 (에어 코리아)
* 테이블 구조 : [pollution_co_concentration_by_station](#pollution_co_concentration_by_station)

<br/>

* 목적:

    전국 도시대기측정망의 2023년 일산화탄소(CO) 농도 측정 결과를 저장합니다.
    측정소 단위로 월별 농도(ppm) 데이터를 보관하며, 대기질 추이 및 지역별 비교 분석에 활용됩니다.

<br/>

* 주요 필드:

    * province: 시도명

    * city: 시군구

    * station_name: 측정소 이름

    * station_code: 측정소 코드

    * jan ~ dec: 1~12월 월별 일산화탄소 농도(ppm)

    * annual_avg: 연평균 CO 농도

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 지역별 공기질 변화 시계열 분석

    * 공원·주거지 인근 대기오염 상관분석

    * 환경 정책 효과 측정


# 전국 도시대기측정망 2023년 미세먼지(PM-10) 농도 측정 결과 (에어 코리아)
* 테이블 구조 : [pollution_co_concentration_by_station](#pollution_co_concentration_by_station)

<br/>

* 목적:

    전국 도시대기측정망의 2023년 미세먼지(PM-10) 농도 측정 결과를 저장합니다.
    측정소 단위로 월별 농도(ppm) 데이터를 보관하며, 대기질 추이 및 지역별 비교 분석에 활용됩니다.

<br/>

* 주요 필드:

    * province: 시도명

    * city: 시군구

    * station_name: 측정소 이름

    * station_code: 측정소 코드

    * jan ~ dec: 1~12월 월별 미세먼지(PM-10) 농도(ppm)

    * annual_avg: 연평균 미세먼지(PM-10) 농도

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 지역별 공기질 변화 시계열 분석

    * 공원·주거지 인근 대기오염 상관분석

    * 환경 정책 효과 측정


# 전국 도시대기측정망 2023년 미세먼지(PM-25) 농도 측정 결과 (에어 코리아)
* 테이블 구조 : [pollution_co_concentration_by_station](#pollution_co_concentration_by_station)

<br/>

* 목적:

    전국 도시대기측정망의 2023년 미세먼지(PM-25) 농도 측정 결과를 저장합니다.
    측정소 단위로 월별 농도(ppm) 데이터를 보관하며, 대기질 추이 및 지역별 비교 분석에 활용됩니다.

<br/>

* 주요 필드:

    * province: 시도명

    * city: 시군구

    * station_name: 측정소 이름

    * station_code: 측정소 코드

    * jan ~ dec: 1~12월 월별 미세먼지(PM-25) 농도(ppm)

    * annual_avg: 연평균 미세먼지(PM-25) 농도

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 지역별 공기질 변화 시계열 분석

    * 공원·주거지 인근 대기오염 상관분석

    * 환경 정책 효과 측정

# 서울시 자치구별 펫세권 관련 업종 데이터

* 테이블 구조 : [pet_friendly_zone_summary](#pet_friendly_zone_summary)

<br/>

* 목적:

    서울시 자치구별 펫세권 관련 업종 데이터를 저장합니다.
    카페, 음식점, 주점 같은 일반 생활 인프라와 함께 동물병원, 펫미용실, 펫용품점, 펫호텔 등 펫 관련 업종 수치를 포함합니다.
    이를 통해 지역별 펫 친화 환경을 정량적으로 비교·분석할 수 있는 기반 데이터를 제공합니다.

<br/>

* 주요 필드:

	* district_name: 자치구명

	* total_places: 전체 업종 수 (카페+음식점+주점+펫 관련)

	* cafe: 카페 수

	* restaurant: 음식점 수

	* pub: 주점 수

	* animal_hospital: 동물병원 수

	* pet_beauty_salon: 펫미용실 수

	* pet_store: 펫용품점 수

	* pet_hotel: 펫호텔 수

	* created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

	* 펫 관련 상권 분포 시각화 및 분석

	* 지역별 펫 인프라 격차 분석

	* 공원/주거환경/인구 데이터와의 교차 분석을 통한 ‘펫세권’ 평가

	* 행정 정책 수립 및 펫 관련 창업 입지 선정 지원


# seoul_pet_welfare_policy 테이블 설명

* 테이블 구조 : [seoul_pet_welfare_policy](#seoul_pet_welfare_policy)

<br/>

* 목적:

    서울시 25개 자치구에서 시행 중인 반려동물 복지 정책을 정리한 정보를 저장합니다.
    정책 항목별로 각 자치구에서 시행 여부를 Boolean 형식으로 기록합니다.

<br/>

* 주요 필드:

    * district_name: 자치구 이름

    * animal_shelter_in_district: 관내 유기동물 보호소 여부

    * dog_playground_or_shelter: 반려견 놀이터 또는 쉼터 존재 여부

    * pet_behavior_education: 반려동물 행동교육 프로그램 운영 여부

    * stray_cat_feeding_station: 길고양이 급식소 운영 여부

    * low_income_vet_support: 취약계층 대상 동물병원 진료 지원

    * pet_temporary_care: 반려동물 임시위탁제도 운영 여부

    * created_at: 데이터 적재 시각

<br/>

* 활용 예시:

    *  정책 수립 시 지역별 복지 정책 분포 시각화

    *  자치구별 반려동물 친화 정책 분석

    *  반려동물 기반 시민 서비스 개선 연구

 
# 전국 반려동물 동반 가능 문화시설 및 반려동물 동반 정보 데이터
* 테이블 구조 : [pet_friendly_culture_facilities](#pet_friendly_culture_facilities)

<br/>

* 목적:
    전국의 반려동물 동반 가능 문화시설(약국, 미술관 등)의 위치 및 반려동물 동반 정보 데이터를 저장합니다.
    시설명, 위치(지번/도로명), 입장 요금, 반려동물 제한사항, 실내외 여부 등 방문 전 필요한 세부 정보를 포함합니다.

<br/>

* 주요 필드:

    * facility_name, sido, sigungu, bunji, can_with_pet, pet_size_allowed, indoors_allowed, outdoors_allowed 등 총 31개 필드

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 반려동물 동반 문화생활 인프라 지도 시각화

    * 실내외 및 시설 종류에 따른 반려견 문화 공간 추천

    * 반려인 관광 편의성 지수 산출 등


# 전국 동물보호센터 기본 정보
* 테이블 구조 : [animal_shelter](#animal_shelter)

<br/>

* 목적:

    전국 동물보호센터의 기본 정보를 저장하는 테이블입니다. 관할구역, 명칭, 연락처, 주소 등의 정보를 포함하며, 지역 기반의 보호시설 인프라 분석 등에 활용됩니다.

<br/>

* 주요 필드:

    * jurisdiction, shelter_name, phone_number, address 등 총 5개 주요 필드

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * GIS 기반 보호센터 분포 시각화

    * 지역별 보호시설 현황 분석

    * 동물복지 인프라 정책 기초 자료

# 서울시 자치구 월평균 소득 및 지출 항목별 금액 정보
테이블 구조 : [seoul_income_expenditure_by_dong](#seoul_income_expenditure_by_dong)

<br/>

* 목적:

    서울시 자치구 단위의 월평균 소득 및 지출 항목별 금액 정보를 저장합니다.
    이 데이터는 소득 구간별 소비 패턴 분석 및 지역별 경제 수준 비교에 활용될 수 있습니다.

<br/>

* 주요 필드:

    * income_avg_monthly (월 평균 소득 금액)

    * expense_total (지출 총금액)

    * expense_food, expense_medical, expense_entertainment 등 항목별 지출

    * created_at: 데이터 적재 일시 자동 기록

<br/>

* 활용 예시:

    * 자치구별 소비 성향 비교

    * 소득 대비 소비 비율 분석

    * 상권 타겟팅 및 마케팅 전략 수립



<br/>
<br/>
<br/>

---

# 테이블 구조 목록




## seoul_animal_hospital
| Variable | Datatype | Info | Note |
|---|---|---|---|
| id | INT |  데이터 ID| PRIMARY KEY |
| open_gov_code | VARCHAR(10) | 개방자치단체코드 ||
| mgmt_num | VARCHAR(50) |관리번호 ||
licensg_de |DATE | 인허가일자 ||
licensg_cncl_de | DATE | 인허가취소일자 ||
status_code | VARCHAR(10) | 영업상태코드 ||
status_name | VARCHAR(50) | 영업상태명 ||
detail_status_code | VARCHAR(10) | 상세영업상태코드 ||
detail_status_name | VARCHAR(50) | 상세영업상태명 ||
close_de | DATE | 폐업일자 ||
suspend_start_de | DATE | 휴업시작일자 ||
suspend_end_de | DATE | 휴업종료일자 ||
reopen_de | DATE | 재개업일자 ||
phone_number | VARCHAR(20) | 전화번호 ||
site_area | FLOAT | 소재지면적 ||
zip_code | VARCHAR(10) | 소재지우편번호 ||
jibun_address | TEXT | 지번주소 ||
road_address | TEXT | 도로명주소 ||
road_zip_code | VARCHAR(10) | 도로명우편번호
bizplc_name | VARCHAR(200) | 사업장명
last_change_de | DATE | 최종수정일자
data_update_type | VARCHAR(20) | 데이터갱신구분
data_update_de | DATE | 데이터갱신일자
category_name | VARCHAR(50) | 업태구분명
x | DECIMAL(15, 8) | 좌표정보(X)
y | DECIMAL(15, 8) | 좌표정보(Y)
livestock_division | VARCHAR(50) | 축산업무구분명
livestock_process_type | VARCHAR(50) | 축산물가공업구분명
livestock_serial_num | VARCHAR(20) | 축산일련번호
right_holder_serial | VARCHAR(20) | 권리주체일련번호
total_personnel | INT | 총인원
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT CURRENT_TIMESTAMP |

## companion_animal_registration
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
sido | VARCHAR(100) | 시도
sigungu | VARCHAR(100) | 시군구
dog_registered_total | INT | 개등록 누계
cat_registered_total | INT | 고양이등록 누계
total_registered | INT | 총 등록 누계
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP

## animal_hospital_registry
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
number | INT | 번호
service_name_open | VARCHAR(255) | 개방서비스명
service_id_open | VARCHAR(255) | 개방서비스아이디
open_gov_code | INT | 개방자치단체코드
mgmt_num | INT | 관리번호
licensg_de | DATE | 인허가일자
licensg_cncl_de | FLOAT | 인허가취소일자
status_code | INT | 영업상태구분코드
status_name | VARCHAR(255) | 영업상태명
detail_status_code | VARCHAR(255) | 상세영업상태코드
detail_status_name | VARCHAR(255) | 상세영업상태명
close_de | DATE | 폐업일자
suspend_start_de | DATE | 휴업시작일자
suspend_end_de | DATE | 휴업종료일자
reopen_de | DATE | 재개업일자
phone_number | VARCHAR(255) | 소재지전화
site_area | FLOAT | 소재지면적
zip_code | FLOAT | 소재지우편번호
jibun_address | VARCHAR(255) | 소재지전체주소
road_address | VARCHAR(255) | 도로명전체주소
road_zip_code | VARCHAR(255) | 도로명우편번호
bizplc_name | VARCHAR(255) | 사업장명
last_change_de | DATE | 최종수정시점
data_update_type | VARCHAR(255) | 데이터갱신구분
data_update_de | DATE | 데이터갱신일자
category_name | FLOAT | 업태구분명
x | FLOAT | 좌표정보x(epsg5174)
y | FLOAT | 좌표정보y(epsg5174)
livestock_division | VARCHAR(255) | 업무구분명
livestock_process_type | FLOAT | 상세업무구분명
right_holder_serial | VARCHAR(255) | 권리주체일련번호
total_personnel | FLOAT | 총직원수
unnamed_32 | FLOAT | Unnamed: 32
created_at | TIMESTAMP  | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP

## animal_beauty_business
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
service_name_open | VARCHAR(100) | 개방서비스명
service_id_open | VARCHAR(100) | 개방서비스아이디
open_gov_code | VARCHAR(10) | 개방자치단체코드
mgmt_num | VARCHAR(50) | 관리번호
licensg_de | DATE | 인허가일자
licensg_cncl_de | DATE | 인허가취소일자
status_code | VARCHAR(10) | 영업상태구분코드
status_name | VARCHAR(50) | 영업상태명
detail_status_code | VARCHAR(10) | 상세영업상태코드
detail_status_name | VARCHAR(50) | 상세영업상태명
close_de | DATE | 폐업일자
suspend_start_de | DATE | 휴업시작일자
suspend_end_de | DATE | 휴업종료일자
reopen_de | DATE | 재개업일자
phone_number_location | VARCHAR(20) | 소재지전화
site_area | FLOAT | 소재지면적
zip_code | VARCHAR(10) | 소재지우편번호
address_jibun | TEXT | 소재지전체주소
road_address | TEXT | 도로명전체주소
road_zip_code | VARCHAR(10) | 도로명우편번호
bizplc_name | VARCHAR(200) | 사업장명
last_change_dt | DATETIME | 최종수정시점
data_update_type | VARCHAR(20) | 데이터갱신구분
data_update_de | DATE | 데이터갱신일자
category_name | VARCHAR(50) | 업태구분명
x | DECIMAL(15 8) | 좌표정보x(epsg5174)
y | DECIMAL(15 8) | 좌표정보y(epsg5174)
work_division | VARCHAR(50) | 업무구분명
work_detail_division | VARCHAR(50) | 상세업무구분명
right_holder_serial | VARCHAR(20) | 권리주체일련번호
total_staff | INT | 총직원수
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP 

## animal_pharmacy_registry
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID |AUTO_INCREMENT <br/> PRIMARY KEY |
service_name_open | VARCHAR(100) | 개방서비스명
service_id_open | VARCHAR(100) | 개방서비스아이디
open_gov_code | VARCHAR(10) | 개방자치단체코드
mgmt_num | VARCHAR(50) | 관리번호
licensg_de | DATE | 인허가일자
licensg_cncl_de | DATE | 인허가취소일자
status_code | VARCHAR(10) | 영업상태구분코드
status_name | VARCHAR(50) | 영업상태명
detail_status_code | VARCHAR(10) | 상세영업상태코드
detail_status_name | VARCHAR(50) | 상세영업상태명
close_de | DATE | 폐업일자
suspend_start_de | DATE | 휴업시작일자
suspend_end_de | DATE | 휴업종료일자
reopen_de | DATE | 재개업일자
phone_number_location | VARCHAR(30) | 소재지전화
site_area | FLOAT | 소재지면적
zip_code | VARCHAR(10) | 소재지우편번호
jibun_address | TEXT | 소재지전체주소
road_address | TEXT | 도로명전체주소
road_zip_code | VARCHAR(10) | 도로명우편번호
bizplc_name | VARCHAR(200) | 사업장명
last_change_de | DATETIME | 최종수정시점
data_update_type | VARCHAR(10) | 데이터갱신구분
data_update_de | DATETIME | 데이터갱신일자
category_name | VARCHAR(100) | 업태구분명
x | DECIMAL(15, 8) | 좌표정보x(epsg5174)
y | DECIMAL(15, 8) | 좌표정보y(epsg5174)
business_type_name | VARCHAR(100) | 업무구분명
business_type_detail | VARCHAR(100) | 상세업무구분명
right_holder_serial | VARCHAR(20) | 권리주체일련번호
total_personnel | INT | 총직원수
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT CURRENT_TIMESTAMP


## seoul_animal_trust_facility
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID |AUTO_INCREMENT <br/> PRIMARY KEY
service_name_open | VARCHAR(100) | 개방서비스명
service_id_open | VARCHAR(100) | 개방서비스아이디
open_gov_code | VARCHAR(10) | 개방자치단체코드
mgmt_num | VARCHAR(50) | 관리번호
licensg_de | DATE | 인허가일자
licensg_cncl_de | DATE | 인허가취소일자
status_code | VARCHAR(10) | 영업상태구분코드
status_name | VARCHAR(50) | 영업상태명
detail_status_code | VARCHAR(10) | 상세영업상태코드
detail_status_name | VARCHAR(50) | 상세영업상태명
close_de | DATE | 폐업일자
suspend_start_de | DATE | 휴업시작일자
suspend_end_de | DATE | 휴업종료일자
reopen_de | DATE | 재개업일자
phone_number_location | VARCHAR(20) | 소재지전화
site_area | FLOAT | 소재지면적
zip_code | VARCHAR(10) | 소재지우편번호
jibun_address | TEXT | 소재지전체주소
road_address | TEXT | 도로명전체주소
road_zip_code | VARCHAR(10) | 도로명우편번호
bizplc_name | VARCHAR(200) | 사업장명
last_change_de | DATE | 최종수정시점
data_update_type | VARCHAR(20) | 데이터갱신구분
data_update_de | DATE | 데이터갱신일자
category_name | VARCHAR(50) | 업태구분명
x | DECIMAL(15, 8) | 좌표정보x(epsg5174)
y | DECIMAL(15, 8) | 좌표정보y(epsg5174)
business_division_name | VARCHAR(100) | 업무구분명
business_detail_division_name | VARCHAR(100) | 상세업무구분명
right_holder_serial | VARCHAR(20) | 권리주체일련번호
total_personnel | INT | 총직원수
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP 

## korea_urban_park_info 
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
mgmt_num |VARCHAR(50) | 관리번호
park_name | VARCHAR(100) | 공원명
park_type | VARCHAR(50) | 공원구분
road_address | TEXT | 소재지도로명주소
jibun_address | TEXT | 소재지지번주소
latitude | DECIMAL(10, 7) | 위도
longitude | DECIMAL(10, 7) | 경도
park_area | FLOAT | 공원면적
facility_sports | TEXT | 공원보유시설(운동시설)
facility_play | TEXT | 공원보유시설(유희시설)
facility_convenience | TEXT | 공원보유시설(편익시설)
facility_culture | TEXT | 공원보유시설(교양시설)
facility_other | TEXT | 공원보유시설(기타시설)
designated_date | DATE | 지정고시일
managing_agency | VARCHAR(100) | 관리기관명
phone_number | VARCHAR(20) | 전화번호
data_reference_date | DATE | 데이터기준일자
provider_code | VARCHAR(20) | 제공기관코드
provider_name | VARCHAR(100) | 제공기관명
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP 

## seoul_abandoned_animal_status
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
district_level_1 | VARCHAR(50) | 자치구별(1)
district_level_2 | VARCHAR(50) | 자치구별(2)
total_count | INT | 전체 유기동물 수
dog_total | INT | 개_소계
dog_returned | INT | 개_인도(주인)
dog_adopted | INT | 개_입양분양
dog_deceased | INT | 개_폐사안락사
dog_other | INT | 개_계류기증
cat_total | INT | 고양이_소계
cat_returned | INT | 고양이_인도(주인)
cat_adopted | INT | 고양이_입양분양
cat_deceased | INT | 고양이_폐사안락사
cat_other | INT | 고양이_계류기증
etc_total | INT | 기타_소계
etc_returned | INT | 기타_인도(주인)
etc_adopted | INT | 기타_입양분양
etc_deceased | INT | 기타_폐사안락사
etc_other | INT | 기타_계류기증
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP 

## seoul_noise_vibration_complaint
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
district_level_1 | VARCHAR(100) | 1차 행정 구역 | (예: 서울특별시)
district_level_2 | VARCHAR(100) | 2차 행정 구역 | (예: 종로구)
total_environmental_complaint | INT | 환경관련 전체 민원 수
noise_vibration_complaint | INT | 소음·진동 민원 수
factory_noise_vibration_complaint | INT | 공장 소음·진동 민원 수
traffic_noise_vibration_complaint | INT | 교통 소음·진동 민원 수
life_noise_vibration_complaint | INT | 생활 소음·진동 민원 수
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP

## pollution_emission_facility
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
region_large |VARCHAR(50) | 지역별(1)
region_small | VARCHAR(50) | 지역별(2)
air_total | INT | 대기(가스·먼지·매연및악취)_소계
air_type_1 | INT | 대기(가스·먼지·매연및악취) 1종
air_type_2 | INT | 대기(가스·먼지·매연및악취) 2종
air_type_3 | INT | 대기(가스·먼지·매연및악취) 3종
air_type_4 | INT | 대기(가스·먼지·매연및악취) 4종
air_type_5 | INT | 대기(가스·먼지·매연및악취) 5종
water_total | INT | 수질(폐수) 소계
water_type_1 | INT | 수질(폐수) 1종
water_type_2 | INT | 수질(폐수) 2종
water_type_3 | INT | 수질(폐수) 3종
water_type_4 | INT | 수질(폐수) 4종
water_type_5 | INT | 수질(폐수) 5종
noise_total | INT | 소음및진동 소계
noise_silent_area | INT | 소음및진동 정온지역
noise_non_silent_area | INT | 소음및진동 정온지역외
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT CURRENT_TIMESTAMP 

## seoul_abandonment_statistics 
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT PRIMARY KEY
district_name | VARCHAR(100) | 자치구명
abandonment_count_2016 | INT | 2016년 유기 동물 발생 건수
abandonment_count_2017 | INT | 2017년 유기 동물 발생 건수
abandonment_count_2018 | INT | 2018년 유기 동물 발생 건수
abandonment_count_2019 | INT | 2019년 유기 동물 발생 건수
abandonment_count_2020 | INT | 2020년 유기 동물 발생 건수
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT CURRENT_TIMESTAMP 


## per_capita_park_area 
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
district_category_1 | VARCHAR(50) | 자치구별(1)
district_category_2 | VARCHAR(50) | 자치구별(2)
park_area_total_sqm_thousands | FLOAT | 공원면적 | (천㎡)
per_capita_park_area_sqm | FLOAT | 1인당 공원면적 | (㎡)
urban_park_area_sqm_thousands | FLOAT | 도시공원면적 | (천㎡)
per_capita_urban_park_area_sqm | FLOAT | 1인당 도시공원면적 | (㎡)
walkable_park_area_sqm_thousands | FLOAT | 도보생활권공원면적 | (천㎡)
per_capita_walkable_park_area_sqm | FLOAT | 1인당 도보생활권공원면적 | (㎡)
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT CURRENT_TIMESTAMP 

## pollution_co_concentration_by_station
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
province | VARCHAR(50) | 시도
city | VARCHAR(50) | 도시
station_name | VARCHAR(100) | 측정소명
station_code | VARCHAR(20) | 측정소코드
january | DECIMAL(5, 2) | 1월
february | DECIMAL(5, 2) | 2월
march | DECIMAL(5, 2) | 3월
april | DECIMAL(5, 2) | 4월
may | DECIMAL(5, 2) | 5월
june | DECIMAL(5, 2) | 6월
july | DECIMAL(5, 2) | 7월
august | DECIMAL(5, 2) | 8월
september | DECIMAL(5, 2) | 9월
october | DECIMAL(5, 2) | 10월
november | DECIMAL(5, 2) | 11월
december | DECIMAL(5, 2) | 12월
annual_avg | DECIMAL(5, 2) | 연평균
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP 


## pollution_pm10_concentration_by_station
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
province | VARCHAR(50) | 시도
city | VARCHAR(50) | 도시
station_name | VARCHAR(100) | 측정소명
station_code | VARCHAR(20) | 측정소코드
january | DECIMAL(5, 2) | 1월
february | DECIMAL(5, 2) | 2월
march | DECIMAL(5, 2) | 3월
april | DECIMAL(5, 2) | 4월
may | DECIMAL(5, 2) | 5월
june | DECIMAL(5, 2) | 6월
july | DECIMAL(5, 2) | 7월
august | DECIMAL(5, 2) | 8월
september | DECIMAL(5, 2) | 9월
october | DECIMAL(5, 2) | 10월
november | DECIMAL(5, 2) | 11월
december | DECIMAL(5, 2) | 12월
annual_avg | DECIMAL(5, 2) | 연평균
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP 


## pollution_pm25_concentration_by_station
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
province | VARCHAR(50) | 시도
city | VARCHAR(50) | 도시
station_name | VARCHAR(100) | 측정소명
station_code | VARCHAR(20) | 측정소코드
january | DECIMAL(5, 2) | 1월
february | DECIMAL(5, 2) | 2월
march | DECIMAL(5, 2) | 3월
april | DECIMAL(5, 2) | 4월
may | DECIMAL(5, 2) | 5월
june | DECIMAL(5, 2) | 6월
july | DECIMAL(5, 2) | 7월
august | DECIMAL(5, 2) | 8월
september | DECIMAL(5, 2) | 9월
october | DECIMAL(5, 2) | 10월
november | DECIMAL(5, 2) | 11월
december | DECIMAL(5, 2) | 12월
annual_avg | DECIMAL(5, 2) | 연평균
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP 


## pet_friendly_zone_summary
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
district_name | VARCHAR(50) | 자치구명 | NOT NULL 
total_places | INT | 전체 장소 수
cafe | INT | 카페 수
restaurant | INT | 음식점 수
pub | INT | 주점 수
animal_hospital | INT | 동물병원 수
pet_beauty_salon | INT | 펫미용실 수
pet_store | INT | 펫용품점 수
pet_hotel | INT | 펫호텔 수
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP

## seoul_pet_welfare_policy
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT PRIMARY KEY | 고유번호
district_name | VARCHAR(50) | 서울시 자치구 이름
animal_shelter_in_district | BOOLEAN | 관내 유기동물 보호소 운영 여부
dog_playground_or_shelter | BOOLEAN | 반려견 전용 놀이터 또는 쉼터 존재 여부
pet_behavior_education | BOOLEAN | 반려동물 행동교육 프로그램 운영 여부
stray_cat_feeding_station | BOOLEAN | 길고양이 공공 급식소 운영 여부
low_income_vet_support | BOOLEAN | 취약계층 대상 동물병원 진료 지원 여부
pet_temporary_care | BOOLEAN | 반려동물 임시위탁제도 운영 여부
created_at | TIMESTAMP | 데이터 적재 일시 | DEFAULT <br/> CURRENT_TIMESTAMP 

## pet_friendly_culture_facilities
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
facility_name | VARCHAR(200) | 시설명
category_lv1 | VARCHAR(50) | 카테고리1
category_lv2 | VARCHAR(50) | 카테고리2
category_lv3 | VARCHAR(50) | 카테고리3
sido | VARCHAR(50) | 시도 명칭
sigungu | VARCHAR(50) | 시군구 명칭
eupmyeon_dong | VARCHAR(50) | 법정읍면동명칭
ri | VARCHAR(50) | 리 명칭
bunji | VARCHAR(100) | 번지
road_name | VARCHAR(100) | 도로명 이름
building_num | VARCHAR(50) | 건물 번호
latitude | DECIMAL(15,8) | 위도
longitude | DECIMAL(15,8) | 경도
zip_code | VARCHAR(10) | 우편번호
road_address | TEXT | 도로명주소
jibun_address | TEXT | 지번주소
phone_number | VARCHAR(50) | 전화번호
homepage | VARCHAR(300) | 홈페이지
closed_days | VARCHAR(100) | 휴무일
operating_hours | VARCHAR(100) | 운영시간
parking_available | VARCHAR(10) | 주차 가능여부
service_price | TEXT | 입장(이용료)가격 정보
can_with_pet | VARCHAR(10) | 반려동물 동반 가능정보
pet_dedicated_info | VARCHAR(100) | 반려동물 전용 정보
pet_size_allowed | VARCHAR(50) | 입장 가능 동물 크기
pet_restrictions | TEXT | 반려동물 제한사항
indoors_allowed | VARCHAR(10) | 장소(실내) 여부
outdoors_allowed | VARCHAR(10) | 장소(실외)여부
description | TEXT | 기본 정보_장소설명
extra_fee_info | VARCHAR(100) | 애견 동반 추가 요금
last_updated | DATE | 최종작성일
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP 

## animal_shelter 
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
seq_num | INT | 번호
jurisdiction | VARCHAR(100) | 관할구역
shelter_name | VARCHAR(200) | 보호센터명
phone_number | VARCHAR(50) | 전화번호
address | TEXT | 주소
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP 

## seoul_income_expenditure_by_dong 
| Variable | Datatype | Info | Note |
|---|---|---|---|
id | INT | 데이터ID | AUTO_INCREMENT <br/> PRIMARY KEY
base_year_quarter_code | VARCHAR(10) | 기준 년분기 코드
admin_dong_code | VARCHAR(10) | 행정동 코드
admin_dong_name | VARCHAR(100) | 행정동 코드 명
income_avg_monthly | INT | 월 평균 소득 금액
income_range_code | VARCHAR(10) | 소득 구간 코드
expense_total | INT | 지출 총금액
expense_food | INT | 식료품 지출 총금액
expense_clothing | INT | 의류 신발 지출 총금액
expense_household | INT | 생활용품 지출 총금액
expense_medical | INT | 의료비 지출 총금액
expense_transport | INT | 교통 지출 총금액
expense_education | INT | 교육 지출 총금액
expense_entertainment | INT | 유흥 지출 총금액
expense_leisure | INT | 여가 문화 지출 총금액
expense_etc | INT | 기타 지출 총금액
expense_dining | INT | 음식 지출 총금액
created_at | TIMESTAMP | 데이터 적재일시 | DEFAULT <br/> CURRENT_TIMESTAMP 
