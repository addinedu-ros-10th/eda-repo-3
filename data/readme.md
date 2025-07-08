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