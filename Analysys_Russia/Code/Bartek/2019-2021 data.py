from Analysys_Russia.Code.Bartek.Main import russian_data,consumptuon_data,pd,np,sns,plt


temp_data_1 = russian_data.copy()
temp_data_2 = consumptuon_data.copy()



temp_data_1 = temp_data_1[['Region','2019', '2020', '2021']]

temp_data_2 = temp_data_2[temp_data_2['Year'].isin([2019, 2020, 2021])]
merged_data = pd.merge(temp_data_1,temp_data_2,on = 'Region',how = 'inner')
merged_data = merged_data.drop(columns=['Mapped_Region'])
merged_data.dropna()
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
print(merged_data.columns)

merged_data.to_csv('regional_alcohol_life_expectancy_2019_2021.csv')

corr_matrix = merged_data.copy()
corr_matrix = corr_matrix.drop(columns=['Region'])
corr_matrix = corr_matrix.corr()

sns.set()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matrix of Correlation for Life Expectancy Analysys')
plt.show()




