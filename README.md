# 🐶🐱 반려동물 행복 주거지 추천 서비스 (TEAM.티니핑)
* '펫세권'으로 제시된 지표를 기반으로 반려동물과 함께 행복하게 살아갈 수 있는 주거지를 찾기 위한 데이터 분석 프로젝트입니다. 서울시 자치구를 대상으로 다양한 공공 및 민간 데이터를 수집/분석하여, 이상적인 반려동물 거주 환경을 평가하고 추천합니다.
<br />

## 0️⃣ 팀구성
### TEAM.티니핑

| 이름 (역할)     | 담당 업무 요약 |
|----------------|----------------|
| 이건창 (팀장)   | 데이터 수집 및 분석, 시각화, 프로젝트 일정·리소스·산출물 관리 |
| 정규호 (팀원)   | 데이터 수집 및 분석, 시각화, DB 설계·구축 및 기술문서 관리 총괄 |
| 박재오 (팀원)   | 데이터 수집 및 분석, 시각화, 기술문서 작성 |
| 이  수 (팀원)    | 데이터 수집 및 분석, 시각화, 기술문서 및 DB 작성 |
| 서지민 (팀원)   | 데이터 수집 및 분석, 시각화, 기술문서 작성 |  


  ## 1️⃣ 사용기술
| 개발환경 | 사용기술 |
|---|---|
| OS | ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)|
| 언어 | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  |
| 데이터 분석 및 시각화 | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=Pandas&logoColor=white) ![Numpy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-301D81?style=for-the-badge&logo=Python&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-50BFDE?style=for-the-badge&logo=Python&logoColor=white) |
| DB관리 |  ![MySql](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white) ![AWS](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white) |
| 협업도구 | ![Confluence](https://img.shields.io/badge/confluence-%23172BF4.svg?style=for-the-badge&logo=confluence&logoColor=white)  ![Slack](https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white) |
| 프로젝트 관리도구|  <img width="99" height="37" alt="Image" src="https://github.com/user-attachments/assets/51b0c6e3-d0f7-4236-a3af-ca66b7fb144f" /> |


## 2️⃣ 펫세권 정의 및 지표
#### 펫세권 정의
'펫세권'은 '역세권'처럼 특정 생활 인프라에 대한 접근성을 강조하는 용어입니다.  
즉, **반려동물을 키우기에 적합한 환경을 갖춘 주거지**를 의미하며, 다음과 같은 요소들을 고려합니다.

* 1인당 도시공원 면적
* 반려동물 관련 서비스업 수
* 대기 질 현황 (미세먼지, 일산화탄소)

#### 펫세권 지표 분류
펫세권을 정의하기 위해 아래와 같은 공공 및 민간 지표들을 활용했습니다.
| 출처 | 펫세권 지표 |
|---|---|
|통계청 SGIS| 1인당 도시공원 면적, 반려동물 관련 서비스업 수, 대기 질 현황(미세먼지, 일산화탄소)|
|다방 (부동산 어플) | 동물병원, 미용실, 반려동물 카페, 반려동물 호텔 |
| KB 부동산 | 카페, 음식점, 주점, 동물병원, 펫미용실, 펫몰, 펫호텔 |


## 3️⃣ 데이터 분석
> 펫세권 지표를 충족한 지역이 실제로 반려동물이 많이 사는 지역인지를 검증하기 위해,  
서울시 자치구별 반려동물 등록수와 펫세권 지표 간의 상관관계를 분석하였습니다.

데이터 분석에 사용된 펫세권 지표들은 다음과 같습니다.
| 연관성 | 지표 |
| --|--|
| 상 | 1인당 도시공원 면적, 반려동물 관련 서비스업 수 |
| 중 | 대기 질 현황 (미세먼지, 일산화탄소) |

### 3.1 단일 데이터 분석
지표 간 스케일 차이를 보정하기 위해 Min-Max Scaling을 적용한 후, 지표별로 반려동물 등록수와의 단순 선형 회귀를 수행하였습니다.  
회귀선의 기울기가 0.5이상인 경우, 강한 경향성을 갖는 것으로 간주하였습니다.

<img width="1426" height="579" alt="Image" src="https://github.com/user-attachments/assets/b2573363-c91e-42d4-a238-35ac0206dd45" />  
<img width="1426" height="579" alt="Image" src="https://github.com/user-attachments/assets/bcf5f45e-f891-470a-aff5-84f1364fd490" />
<br />
<br />

|경향성|지표|
|--|--|
|**강함**|미용 업체 수, 위탁 업체 수, 병원 수, 미세먼지 농도|
|약함|1인당 도시공원 면적, CO 농도|

단일 데이터로 비교했을 경우, 펫세권으로 제시된 지표가 반려동물 등록수와 경향성이 있는것으로 분석되었으며, 다중 데이터를 비교하는 과정을 통해 타당한 분석이었는지를 확인하였습니다.

---
### 3.2 다중 데이터 분석

---

### 3.3 반려동물 이상적 주거지 분석

---

## 4️⃣ 견종별 주거지 추천 서비스


