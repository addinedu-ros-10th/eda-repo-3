df_stacked = df.set_index('자치구명').T
df_stacked.index = df_stacked.index.str.extract(r'(\d{4})')[0].astype(int)
df_stacked = df_stacked.astype(int)

df_stacked.T.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='tab20')
plt.title('✅ 연도별 자치구 누적 유기견 발생 건수', fontsize=16)
plt.ylabel('유기견 건수')
plt.xlabel('자치구')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
