from Code.Bartek.Main import russian_data,plt,sns


temp_data = russian_data.copy()

temp_data.drop(columns=['Year','2019','2020','2021'], inplace=True)
temp_data.dropna(inplace=True)
print(len(temp_data['males ']))


corr_matrix = temp_data.corr()
sns.set()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matrix of Correlation for Russia Analysys')
plt.show()


