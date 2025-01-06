import pandas as pd
from pandas.core.config_init import max_cols
from Analysys_Russia.Code.Bartek.Main import russian_data, plt, sns

temp_data = russian_data.copy()
temp_data.drop(columns=['Year', '2019', '2020', '2021', 'Region'], inplace=True)
temp_data.dropna(inplace=True)

print(len(temp_data['males ']))

corr_matrix = temp_data.corr()

pd.set_option('display.max_columns', None)

print(corr_matrix)

sns.set()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matrix of Correlation for Russia Analysis')
plt.show()
