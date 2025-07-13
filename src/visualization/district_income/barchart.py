import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

# 데이터 로드 및 최신 분기 필터링
df = pd.read_csv("DATA/서울시 상권분석서비스(소득소비-자치구).csv", encoding='cp949')
latest_quarter = df['기준_년분기_코드'].max()
latest_df = df[df['기준_년분기_코드'] == latest_quarter]

# 바차트 시각화
plt.figure(figsize=(12, 6))
sns.barplot(data=latest_df.sort_values('월_평균_소득_금액', ascending=False), x='행정동_코드_명', y='월_평균_소득_금액', color='skyblue', label='월평균소득')
sns.barplot(data=latest_df.sort_values('월_평균_소득_금액', ascending=False), x='행정동_코드_명', y='지출_총금액', color='salmon', alpha=0.6, label='총지출금액')
plt.xticks(rotation=45)
plt.title('자치구별 월평균 소득 및 총 소비 금액')
plt.ylabel('금액 (원)')
plt.legend()
plt.tight_layout()
plt.show()
