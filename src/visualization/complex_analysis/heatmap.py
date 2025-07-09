import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import os

# CSV 파일 로드
df = pd.read_csv("DATA/total_score_reg_in_rank_update.csv")  # 파일명은 실제 파일명으로 수정
# df = pd.read_csv("DATA/total_score_update.csv")  # 파일명은 실제 파일명으로 수정

# 자치구 이름을 인덱스로 설정
df.set_index('자치구', inplace=True)

# 종합 점수와 개별 요소 간 상관계수 계산
corr_matrix = df.corr(numeric_only=True)

# 히트맵 시각화
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', fmt='.2f', linewidths=0.5)
plt.title("자치구 주요 지표 간 상관관계 Heatmap", fontsize=16)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/total_score_heatmap.png'
# output_path = 'RESULT/visualization/서울_자치구별_반려동물_관련_지표_비교_(정규화 스케일)_1인당_공원면적.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()
