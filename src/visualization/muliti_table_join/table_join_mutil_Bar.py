
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import numpy as np



# 데이터 불러오기
df = pd.read_csv("/home/qatest/eda/eda-repo-3/RESULT/csv/seoul_integrated_data.csv")

# 필요한 컬럼 선택
selected_df = df[['district', 
                  'companion_animal_registration', 
                  'seoul_noise_vibration_complaint', 
                  'pollution_co_concentration_by_station', 
                  'pollution_emission_facility']]

# selected_df = selected_df.sort_values(by='district' , ascending=True)
# selected_df = selected_df.sort_values(by='companion_animal_registration' , ascending=True)
selected_df = selected_df.sort_values(by=['district', 'pollution_co_concentration_by_station'], ascending=[True, True])

selected_df.set_index('district', inplace=True)

labels = selected_df.index.tolist()
x = np.arange(len(labels))
width = 0.2

fig, ax1 = plt.subplots(figsize=(16, 8))

# 메인 y축 (left)
rects1 = ax1.bar(x - 1.5*width, selected_df['companion_animal_registration'], width, label='반려동물 등록')
rects2 = ax1.bar(x - 0.5*width, selected_df['seoul_noise_vibration_complaint'], width, label='소음/진동 민원')
rects4 = ax1.bar(x + 1.5*width, selected_df['pollution_emission_facility'], width, label='오염물 배출시설')

ax1.set_ylabel('등록/민원/시설 수')
ax1.set_xlabel('자치구')
ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=45, ha='right')

# 보조 y축 (right)
ax2 = ax1.twinx()
rects3 = ax2.bar(x + 0.5*width, selected_df['pollution_co_concentration_by_station'], width, color='orange', label='CO 농도')
ax2.set_ylabel('CO 농도(ppm)')

# 범례 합치기
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper left')

ax1.set_title('지역구 및 소음,진동,오영물배출시설 (CO 농도는 우측 축)다중막대그래프.png')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# ▶️ 이미지 저장 경로 지정
output_path = '/home/qatest/eda/eda-repo-3/RESULT/visualization/지역구_소음_진동_오영물배출시설_CO농도_다중막대그래프.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 폴더가 없으면 생성
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # 고해상도 저장

plt.show()
