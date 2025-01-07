from Analysys_Russia.Code.Bartek.Main import russian_data, np, sns, plt

def MNK(x, y):
    x_2 = x ** 2
    A = np.array([[x_2.sum(), x.sum()], [x.sum(), len(x)]])
    B = np.array([(x * y).sum(), y.sum()])
    find = np.linalg.inv(A).dot(B)
    return find

salary_data = russian_data.copy()
salary_data = salary_data[['Region', 'Wine', 'Brandy']].dropna()
salary_data = salary_data[(salary_data['Wine'] != 5136.550000) & (salary_data['Brandy'] != 5136.550000)]
salary_data = salary_data.sort_values(by='Wine')

sns.set()
fig, ax1 = plt.subplots(figsize=(10,8))

x_wine = np.arange(len(salary_data))
y_wine = salary_data['Wine'].values
reg_wine = MNK(x_wine, y_wine)
y_wine_reg = reg_wine[0] * x_wine + reg_wine[1]

ax1.scatter(salary_data['Region'], y_wine, color='#2A9E6D', label='Wine')
ax1.set_xlabel('Region')
ax1.set_ylabel('Wine Consumption', color='black')
ax1.tick_params(axis='y', labelcolor='#2A9E6D')
ax1.set_xticks(range(len(salary_data['Region'])))
ax1.set_xticklabels(salary_data['Region'], rotation=45, ha='right', fontsize=6)

ax1.plot(salary_data['Region'], y_wine_reg, color='#2A9E6D', linestyle='--')

ax2 = ax1.twinx()

x_brandy = np.arange(len(salary_data))
y_brandy = salary_data['Brandy'].values
reg_brandy = MNK(x_brandy, y_brandy)
y_brandy_reg = reg_brandy[0] * x_brandy + reg_brandy[1]

ax2.scatter(salary_data['Region'], y_brandy, color='#9E2A2F', label='Brandy')
ax2.set_ylabel('Brandy Consumption', color='black')
ax2.tick_params(axis='y', labelcolor='#9E2A2F')

ax2.plot(salary_data['Region'], y_brandy_reg, color='#9E2A2F', linestyle='--')

plt.title('Wine and Brandy Consumption by Region')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()

