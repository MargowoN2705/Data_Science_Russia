from Analysys_Russia.Code.Bartek.Main import russian_data, pd, np, sns, plt

temp_data = russian_data.copy()
temp_data = temp_data.dropna()
print(temp_data.columns)
temp_data = temp_data.sort_values(by='Salary')
temp_data = temp_data[['Salary', 'GRDP_per_capita' ,'Region']]

print(temp_data.describe())

sns.set()
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

bar_grdp = ax1.bar(temp_data['Region'], temp_data['GRDP_per_capita'], color='green', label='GDP per capita')

scatter_salary = ax2.scatter(temp_data['Region'], temp_data['Salary'], color='blue', label='Average salary', s=100)

ax1.set_ylabel('GDP per capita (RUB)', fontsize=12, color='green')
ax2.set_ylabel('Average salary (RUB)', fontsize=12, color='blue')
plt.title('Relationship between GDP per capita and average salary by region', fontsize=16)

ax1.set_xticks(np.arange(len(temp_data['Region'])))
ax1.set_xticklabels(temp_data['Region'], rotation=45, ha='right')

ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7)
fig.legend(loc='upper right', bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)

fig.tight_layout()
plt.show()
