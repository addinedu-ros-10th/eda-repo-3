# 🐶🐱 반려동물 행복 주거지 추천 서비스 (TEAM.티니핑)
* '펫세권'으로 제시된 지표를 기반으로 반려동물과 함께 행복하게 살아갈 수 있는 주거지를 찾기 위한 데이터 분석 프로젝트입니다. 
* 서울시 자치구를 대상으로 다양한 공공 및 민간 데이터를 수집/분석하여, 이상적인 반려동물 거주 환경을 평가하고 추천합니다.
<br />

## 0️⃣ 팀구성 
### TEAM.티니핑

| 이름 (역할)     | 담당 업무 요약 |
|----------------|----------------|
| **이건창 (팀장)**   | 데이터 수집 및 분석, 시각화, 프로젝트 총 관리 |
| **정규호 (팀원)**   | 데이터 수집 및 분석, 시각화, DB 설계·구축 및 기술문서 관리 총괄 |
| **박재오 (팀원)**   | 데이터 수집 및 분석, 시각화, 기술문서 작성 |
| **이 수 (팀원)**    | 데이터 수집 및 분석, 시각화, 기술문서 및 DB 작성 |
| **서지민 (팀원)**   | 데이터 수집 및 분석, 시각화, 기술문서 작성 |  


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
> #### 펫세권 정의
'펫세권'은 **반려동물을 키우기에 적합한 환경을 갖춘 주거지**를 의미함

> #### 펫세권 지표 분류
* 공공 및 민간 지표 활용

| 출처 | 펫세권 지표 |
|---|---|
|**통계청 SGIS**| 1인당 도시공원 면적, 반려동물 관련 서비스업 수, 대기 질 현황(미세먼지, 일산화탄소)|
|**다방 (부동산 어플)** | 동물병원, 미용실, 반려동물 카페, 반려동물 호텔 |
| **KB 부동산** | 카페, 음식점, 주점, 동물병원, 펫미용실, 펫몰, 펫호텔 |


## 3️⃣ 데이터 분석
* 3.1 펫세권·반려동물 등록수 경향성
* 3.2 통계청, 다방, KB 부동산 펫세권 타당성 검토 
* 3.3 반려동물 이상적 주거지 분석


### 3.1 펫세권·반려동물 등록수 경향성
* Min-Max Scaling으로 정규화 적용
* **회귀선 기울기 > 0.5** 인 경우, 강한 경향성으로 판단

<img width="1110" height="450" alt="Image" src="https://github.com/user-attachments/assets/8cee6171-b1f0-4349-8ab1-5348b7bc12d8" />  


<img width="1110" height="450" alt="Image" src="https://github.com/user-attachments/assets/41c59ac7-0011-4eb7-99b7-a061419f63f7" />



<br />
<br />

|경향성|지표|
|--|--|
|**강함**|미용 업체 수, 위탁 업체 수, 병원 수, 미세먼지 농도|
|약함|1인당 도시공원 면적, CO 농도|

> ###  결론
* 총 6개 지표 중 4개에서 **기울기 > 0.5**로 상대적으로 강한 양의 경향성 확인
* 일부 지표와의 상관관계가 존재함을 나타내며, 이후 단계에서 정밀 분석진행

---
### 3.2 통계청, 다방, KB 부동산 펫세권 타당성 검토 

>  통계청 펫세권 타당성 검토
* 통계청에서 제시한 펫세권 기반으로 추천한 지역과 반려동물 등록수 비교

<img width="1426" height="579" alt="Screenshot from 2025-07-13 23-21-30" src="https://github.com/user-attachments/assets/dadbf402-0468-4307-9d9e-2a5bb61026d1" />  

<img width="1426" height="579" alt="Screenshot from 2025-07-13 23-25-33" src="https://github.com/user-attachments/assets/2ee6a514-9333-473d-9f81-aa6cab1a3444" />

* 추천 받은 지역의 반려동물 등록수 3만 > 비추천 지역의 반려동물 등록수 2만
* 통계청에서 펫세권 기반으로 추천한 지역과 반려동물 등록수 간의 연관성 확인  


> 다방, KB부동산 펫세권 타당성 검토

<img width="1426" height="579" alt="Screenshot from 2025-07-13 23-29-08" src="https://github.com/user-attachments/assets/633a9b68-2f62-44fb-a257-f560c592e7d7" />  

<img width="800" height="500" alt="Screenshot from 2025-07-13 23-30-04" src="https://github.com/user-attachments/assets/ac0e5848-35ac-4027-b620-4bfebcd8390f" />

* '펫 시설수'와 '반려동물 등록수' 연관성 약함

> ### 결론
* **통계청 데이터** '**주 데이터**'로 분석에 활용
* 다방 / KB 부동산 '보조 데이터'로 분석에 활용
---

### 3.3 반려동물 이상적 주거지 분석

> 주거지 분석 8가지 기준
* 건강
* 서비스
* 녹지
* 대기질
* 스트레스
* 오염
* 위험
* 복지

<img width="600" height="600" alt="Screenshot from 2025-07-13 23-45-53" src="https://github.com/user-attachments/assets/332d3056-5c12-4eae-9cea-c875a4655f6c" />

* 긍정 요인 (+) : 건강, 서비스, 녹지
* 부정 요인 (-) : 위험

> 긍정 요인만 고려한 주거지 순위  

<img width="400" height="400" alt="Screenshot from 2025-07-13 23-52-23" src="https://github.com/user-attachments/assets/8f48d008-af77-4ec4-8185-e9bb13d3d0b2" />

* 각 분야 별 1위 ~ 5위 지역에, 5점 ~ 1점 순 배점

> 부정 요인만 고려한 주거지 순위  

<img width="400" height="400" alt="Screenshot from 2025-07-13 23-56-54" src="https://github.com/user-attachments/assets/0abf1f58-5ed7-4914-821a-e22f4657b28d" />

* 각 분야 별 1위 ~ 5위 지역에, 5점 ~ 1점 순 배점

|자치구(긍정)|순위|자치구(부정)
|--|--|--|
|강남구|1위|관악구|
|서초구|2위|강서구|
|송파구|3위|도봉구|
|종로구|4위|양천구|
|마포구|5위|서초구|
---

## 4️⃣ 테마별 반려동물 주거지 추천 서비스


=======

---

## 5️⃣ 견종별 주거지 추천 서비스
=======