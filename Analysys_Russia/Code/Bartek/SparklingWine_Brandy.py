from matplotlib.pyplot import xticks
from Analysys_Russia.Code.Bartek.Main import consumptuon_data,russian_data, pd, np, sns, plt

def MNK(x, y):
    x_2 = x ** 2
    A = np.array([[x_2.sum(), x.sum()], [x.sum(), len(x)]])
    B = np.array([(x * y).sum(), y.sum()])
    find = np.linalg.inv(A).dot(B)
    return find

temp_data = consumptuon_data.copy()
temp_data = temp_data.loc[temp_data['Year'] == 2022]
temp_data = temp_data[['Region', 'Sparkling wine', 'Brandy']]
temp_data = temp_data.sort_values(by='Sparkling wine')

sns.set()
fig, ax1 = plt.subplots(figsize=(10,8))

x_sparkling = np.arange(len(temp_data))
y_sparkling = temp_data['Sparkling wine'].values
reg_sparkling = MNK(x_sparkling, y_sparkling)
y_sparkling_reg = reg_sparkling[0] * x_sparkling + reg_sparkling[1]

ax1.scatter(temp_data['Region'], y_sparkling, color='#2A9E6D', label='Sparkling Wine')
ax1.set_xlabel('Region')
ax1.set_ylabel('Sparkling Wine Consumption', color='black')
ax1.tick_params(axis='y', labelcolor='#2A9E6D')
ax1.set_xticks(range(len(temp_data['Region'])))
ax1.set_xticklabels(temp_data['Region'], rotation=45, ha='right', fontsize=6)

ax1.plot(temp_data['Region'], y_sparkling_reg, color='#2A9E6D', linestyle='--')

ax2 = ax1.twinx()

y_brandy = temp_data['Brandy'].values
reg_brandy = MNK(x_sparkling, y_brandy)
y_brandy_reg = reg_brandy[0] * x_sparkling + reg_brandy[1]

ax2.scatter(temp_data['Region'], y_brandy, color='#9E2A2F', label='Brandy')
ax2.set_ylabel('Brandy Consumption', color='black')
ax2.tick_params(axis='y', labelcolor='#9E2A2F')

ax2.plot(temp_data['Region'], y_brandy_reg, color='#9E2A2F', linestyle='--')

plt.title('Sparkling Wine vs Brandy Consumption by Region in 2022')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()
