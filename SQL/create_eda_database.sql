/* =============================================================
   Collation: utf8mb4_0900_ai_ci
   -------------------------------------------------------------
   • Character set : utf8mb4  (표준 4-바이트 UTF-8 → 모든 유니코드·이모지 지원)
   • Unicode base  : UCA 9.0  (최신 정렬 규칙, 다국어 정확도 ↑)
   • _ai           : accent-insensitive  → 'e' = 'é'
   • _ci           : case-insensitive    → 'A' = 'a'
   • MySQL 8.x 기본값 — 한국어/영어/이모지 혼합 데이터 권장
   ============================================================ */

-- EDA 프로젝트 전용 데이터베이스 생성
CREATE DATABASE eda
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

-- 서울 동물 병원 테이블 생성
CREATE TABLE seoul_animal_hospital (
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
