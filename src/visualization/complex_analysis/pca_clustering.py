import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import koreanize_matplotlib
import os

# 데이터 로드
df = pd.read_csv("DATA/total_score_update.csv")
features = df.drop(columns=['자치구'])  # 점수만 추출
districts = df['자치구']

# 정규화 (스케일링)
scaler = StandardScaler()
scaled = scaler.fit_transform(features)

# PCA로 2차원 축소
pca = PCA(n_components=2)
pca_components = pca.fit_transform(scaled)

# KMeans 클러스터링
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(pca_components)

# 시각화
plt.figure(figsize=(10, 8))
for i in range(len(districts)):
    plt.text(pca_components[i, 0], pca_components[i, 1], districts[i], fontsize=9,
             bbox=dict(facecolor='white', alpha=0.6, edgecolor='gray'))

plt.scatter(pca_components[:, 0], pca_components[:, 1], c=clusters, cmap='Set2', s=50, alpha=0.7)
plt.title("자치구 유사도 기반 클러스터링 (KMeans + PCA)", fontsize=15)
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.grid(True)
plt.tight_layout()

# ▶️ 이미지 저장 경로 지정
output_path = 'RESULT/visualization/pca_clustering.png'
# output_path = 'RESULT/visualization/서울_자치구별_반려동물_관련_지표_비교_(정규화 스케일)_1인당_공원면적.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()
