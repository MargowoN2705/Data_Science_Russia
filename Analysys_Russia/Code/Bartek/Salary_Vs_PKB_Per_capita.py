from Analysys_Russia.Code.Bartek.Main import russian_data, pd, np, sns, plt

def MNK(x, y):
    x_2 = x ** 2
    A = np.array([[x_2.sum(), x.sum()], [x.sum(), len(x)]])
    B = np.array([(x * y).sum(), y.sum()])
    find = np.linalg.inv(A).dot(B)
    return find

temp_data = russian_data.copy()

print(temp_data.columns)
temp_data = temp_data.sort_values(by='Salary')
temp_data = temp_data[['Salary', 'GRDP_per_capita' ,'Region']].dropna()

print(temp_data.describe())

regression_salary = MNK(np.arange(len(temp_data['Region'])), temp_data['Salary'])
regression_grdp = MNK(np.arange(len(temp_data['Region'])), temp_data['GRDP_per_capita'])

sns.set()
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

bar_grdp = ax1.bar(temp_data['Region'], temp_data['GRDP_per_capita'], color='#1d6e33', label='GDP per capita')
scatter_salary = ax2.scatter(temp_data['Region'], temp_data['Salary'], color='#5a9bd5', label='Average salary', s=100)

x_line = np.arange(len(temp_data['Region']))
y_line_salary = regression_salary[0] * x_line + regression_salary[1]
y_line_grdp = regression_grdp[0] * x_line + regression_grdp[1]

ax2.plot(temp_data['Region'], y_line_salary, color='#347bbd', linestyle='--', label='Salary Regression')
ax1.plot(temp_data['Region'], y_line_grdp, color='#1d6e33', linestyle='--', label='GRDP Regression')

ax1.set_ylabel('GDP per capita (RUB)', fontsize=12, color='green')
ax2.set_ylabel('Average salary (RUB)', fontsize=12, color='blue')
plt.title('Relationship between GDP per capita and average salary by region', fontsize=16)

ax1.set_xticks(np.arange(len(temp_data['Region'])))
ax1.set_xticklabels(temp_data['Region'], rotation=45, ha='right')

ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7)
fig.legend(loc='upper left')

fig.tight_layout()
plt.show()


sns.set()
fig, ax1 = plt.subplots(figsize=(14, 8))
temp_data = temp_data[(temp_data['Salary'] != 127.145000) & (temp_data['GRDP_per_capita'] != 2182.863000)]
scatter_grdp_salary = ax1.scatter(temp_data['GRDP_per_capita'], temp_data['Salary'], color='#1d6e33', label='Average salary', s=100)

regression_ = MNK(temp_data['GRDP_per_capita'], temp_data['Salary'])
y_line_2 = regression_[0] * temp_data['GRDP_per_capita'] + regression_[1]
ax1.plot(temp_data['GRDP_per_capita'], y_line_2, color='#347bbd', linestyle='--', label='Regression')

ax1.set_xlabel('GDP per capita (RUB)', fontsize=12, color='black')
ax1.set_ylabel('Average salary (RUB)', fontsize=12, color='black')
plt.title('Relationship between Average salary and GDP per capita by region', fontsize=16)


ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7)
fig.tight_layout()
plt.show()
