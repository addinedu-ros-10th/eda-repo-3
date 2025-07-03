위 데이터를 적재할 table 을 생성하고 싶어.
파일의 컬럼명을 필드별 description으로 사용해줘.
한글로 작성 된 파일의 컬럼명을 영어로 번역해서 테이블 필드명으로 사용해줘.
테이블 필드명은 모두 영문을 사용해서 작성해줘.

다음과 같은 정책으로 필드명을 구성합니다:

standardized_field_schema에서 이미 등록된 한글 필드는 영문 필드명 그대로 사용

등록되지 않은 한글 컬럼명은 영문으로 의미 기반 번역

예: 개방서비스명 → service_name_open

예: 소재지전화 → phone_number_location

이후 변환된 필드명을 기반으로 완전한 영문 테이블 SQL을 다시 생성합니다.


Auto increment id 필드를 PK로 하는 테이블 Create table sql 을 만들어줘.

standardized_field_schema 테이블에는 다음과 같은 정보가 들어 있어.
mysql> select * from standardized_field_schema;
+----+-----------------------+------------------------+-----------------------------+---------------------+
| id | table_name            | field_name             | field_description           | created_at          |
+----+-----------------------+------------------------+-----------------------------+---------------------+
|  1 | seoul_animal_hospital | open_gov_code          | 개방자치단체코드            | 2025-07-03 02:19:55 |
|  2 | seoul_animal_hospital | mgmt_num               | 관리번호                    | 2025-07-03 02:19:55 |
|  3 | seoul_animal_hospital | licensg_de             | 인허가일자                  | 2025-07-03 02:19:55 |
|  4 | seoul_animal_hospital | licensg_cncl_de        | 인허가취소일자              | 2025-07-03 02:19:55 |
|  5 | seoul_animal_hospital | status_code            | 영업상태코드                | 2025-07-03 02:19:55 |
|  6 | seoul_animal_hospital | status_name            | 영업상태명                  | 2025-07-03 02:19:55 |
|  7 | seoul_animal_hospital | detail_status_code     | 상세영업상태코드            | 2025-07-03 02:19:55 |
|  8 | seoul_animal_hospital | detail_status_name     | 상세영업상태명              | 2025-07-03 02:19:55 |
|  9 | seoul_animal_hospital | close_de               | 폐업일자                    | 2025-07-03 02:19:55 |
| 10 | seoul_animal_hospital | suspend_start_de       | 휴업시작일자                | 2025-07-03 02:19:55 |
| 11 | seoul_animal_hospital | suspend_end_de         | 휴업종료일자                | 2025-07-03 02:19:55 |
| 12 | seoul_animal_hospital | reopen_de              | 재개업일자                  | 2025-07-03 02:19:55 |
| 13 | seoul_animal_hospital | phone_number           | 전화번호                    | 2025-07-03 02:19:55 |
| 14 | seoul_animal_hospital | site_area              | 소재지면적                  | 2025-07-03 02:19:55 |
| 15 | seoul_animal_hospital | zip_code               | 소재지우편번호              | 2025-07-03 02:19:55 |
| 16 | seoul_animal_hospital | jibun_address          | 지번주소                    | 2025-07-03 02:19:55 |
| 17 | seoul_animal_hospital | road_address           | 도로명주소                  | 2025-07-03 02:19:55 |
| 18 | seoul_animal_hospital | road_zip_code          | 도로명우편번호              | 2025-07-03 02:19:55 |
| 19 | seoul_animal_hospital | bizplc_name            | 사업장명                    | 2025-07-03 02:19:55 |
| 20 | seoul_animal_hospital | last_change_de         | 최종수정일자                | 2025-07-03 02:19:55 |
| 21 | seoul_animal_hospital | data_update_type       | 데이터갱신구분              | 2025-07-03 02:19:55 |
| 22 | seoul_animal_hospital | data_update_de         | 데이터갱신일자              | 2025-07-03 02:19:55 |
| 23 | seoul_animal_hospital | category_name          | 업태구분명                  | 2025-07-03 02:19:55 |
| 24 | seoul_animal_hospital | x                      | 좌표정보(X)                 | 2025-07-03 02:19:55 |
| 25 | seoul_animal_hospital | y                      | 좌표정보(Y)                 | 2025-07-03 02:19:55 |
| 26 | seoul_animal_hospital | livestock_division     | 축산업무구분명              | 2025-07-03 02:19:55 |
| 27 | seoul_animal_hospital | livestock_process_type | 축산물가공업구분명          | 2025-07-03 02:19:55 |
| 28 | seoul_animal_hospital | livestock_serial_num   | 축산일련번호                | 2025-07-03 02:19:55 |
| 29 | seoul_animal_hospital | right_holder_serial    | 권리주체일련번호            | 2025-07-03 02:19:55 |
| 30 | seoul_animal_hospital | total_personnel        | 총인원                      | 2025-07-03 02:19:55 |
| 31 | seoul_animal_hospital | created_at             | 데이터 적재일시             | 2025-07-03 02:19:55 |
+----+-----------------------+------------------------+-----------------------------+---------------------+

표준화된 영문 필드명 사용할 수 있으면 기존 필드명으로 테이블 필드명을 구성해줘.
없는 경우에는 한글 컬럼명을 영문으로 번역해서 표준화 영문 필드명을 생성해 사용해줘.

그리고 표준화된 필드명과 description을 관리 할 수 있는 표준화 스키마 테이블에 신규로 생성된 표준화 필드명을 적재할 수 있도록 Insert SQL을 제공해줘.

첨부한 파일을 적재할 수 있는, Auto increment id 필드를 PK로 하는 테이블 Create table sql 을 만들어줘.

그리고 테이블 정보를 문서화 할 수 있게 아래와 같은 형식으로 정보를 구조화해줘.

✅ seoul_animal_hospital 테이블 설명
테이블명: seoul_animal_hospital

목적:
서울시 공공데이터에서 제공하는 동물병원 인허가 정보를 저장합니다.
인허가 일자, 폐업/휴업 상태, 병원 위치, 좌표, 업종 구분 등 상세한 행정 데이터를 포함합니다.

주요 필드:

licensg_de, status_name, jibun_address, x, y, 등 총 31개 필드

created_at: 데이터 적재 일시 자동 기록

활용 예시:

반려동물 관련 의료 인프라 분석

GIS 기반 병원 위치 시각화

서울시 각 구역별 동물병원 운영 현황 분석

✅ seoul_animal_hospital MySQL 테이블 생성 SQL



CREATE TABLE seoul_animal_hospital (
    id INT AUTO_INCREMENT PRIMARY KEY,
    open_gov_code VARCHAR(10) COMMENT '개방자치단체코드',
    mgmt_num VARCHAR(50) COMMENT '관리번호',
    licensg_de DATE COMMENT '인허가일자',
    licensg_cncl_de DATE COMMENT '인허가취소일자',
    status_code VARCHAR(10) COMMENT '영업상태코드',
    status_name VARCHAR(50) COMMENT '영업상태명',
    detail_status_code VARCHAR(10) COMMENT '상세영업상태코드',
    detail_status_name VARCHAR(50) COMMENT '상세영업상태명',
    close_de DATE COMMENT '폐업일자',
    suspend_start_de DATE COMMENT '휴업시작일자',
    suspend_end_de DATE COMMENT '휴업종료일자',
    reopen_de DATE COMMENT '재개업일자',
    phone_number VARCHAR(20) COMMENT '전화번호',
    site_area FLOAT COMMENT '소재지면적',
    zip_code VARCHAR(10) COMMENT '소재지우편번호',
    jibun_address TEXT COMMENT '지번주소',
    road_address TEXT COMMENT '도로명주소',
    road_zip_code VARCHAR(10) COMMENT '도로명우편번호',
    bizplc_name VARCHAR(200) COMMENT '사업장명',
    last_change_de DATE COMMENT '최종수정일자',
    data_update_type VARCHAR(20) COMMENT '데이터갱신구분',
    data_update_de DATE COMMENT '데이터갱신일자',
    category_name VARCHAR(50) COMMENT '업태구분명',
    x DECIMAL(15, 8) COMMENT '좌표정보(X)',
    y DECIMAL(15, 8) COMMENT '좌표정보(Y)',
    livestock_division VARCHAR(50) COMMENT '축산업무구분명',
    livestock_process_type VARCHAR(50) COMMENT '축산물가공업구분명',
    livestock_serial_num VARCHAR(20) COMMENT '축산일련번호',
    right_holder_serial VARCHAR(20) COMMENT '권리주체일련번호',
    total_personnel INT COMMENT '총인원',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '데이터 적재일시'
) COMMENT='서울시 동물병원 인허가 정보 테이블';
