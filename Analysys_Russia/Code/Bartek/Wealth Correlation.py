from Analysys_Russia.Code.Bartek.Main import russian_data,plt,sns,np,pd


temp_data = russian_data.copy()
desired_columns = ['males ', 'females ',  'population ',
                   'GRDP_per_capita', 'Density', 'GRDP', 'Total consumption for Region', 'Salary']


wealth = temp_data[desired_columns]

print(wealth.columns)

corr_matrix = wealth.copy()
corr_matrix = corr_matrix.corr()
sns.set()

plt.figure(figsize=(15, 12))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matrix of Correlation for Weatlh in Regions of Russia')
plt.show()
