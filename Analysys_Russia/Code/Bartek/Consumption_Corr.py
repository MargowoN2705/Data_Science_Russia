from Analysys_Russia.Code.Bartek.Main import consumptuon_data, plt, pd, np, sns

corr_matrix = consumptuon_data.copy()

corr_matrix = corr_matrix.drop(columns=['Region'])
corr_matrix = corr_matrix.drop(columns=['Mapped_Region'])

corr_matrix = corr_matrix.corr()
sns.set()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matrix of Correlation for Life Alkohol Consumption in 2017 - 2023')
plt.show()
