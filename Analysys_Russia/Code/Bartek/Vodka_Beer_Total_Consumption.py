from Analysys_Russia.Code.Bartek.Main import consumptuon_data, plt, pd, sns, np

def MNK(x, y):
    x_2 = x ** 2
    A = np.array([[x_2.sum(), x.sum()], [x.sum(), len(x)]])
    B = np.array([(x * y).sum(), y.sum()])
    find = np.linalg.inv(A).dot(B)
    return find

temp_data = consumptuon_data.copy()
temp_data = temp_data[temp_data['Year'] == 2022]
temp_data = temp_data[['Region', 'Vodka', 'Beer', 'Total alcohol consumption (in liters of pure alcohol per capita)']]
temp_data = temp_data.sort_values(by='Total alcohol consumption (in liters of pure alcohol per capita)', ascending=False)

sns.set()

fig, ax1 = plt.subplots(figsize=(12, 8))
ax2 = ax1.twinx()

vodka_scatter = ax1.scatter(temp_data['Region'], temp_data['Vodka'], color='blue', label='Vodka', edgecolors='black')
total_consumption_scatter = ax2.scatter(temp_data['Region'], temp_data['Total alcohol consumption (in liters of pure alcohol per capita)'], color='red', label='Total Consumption', edgecolors='black')

ax1.set_ylabel('Vodka Consumption', fontsize=10, color='black')
ax2.set_ylabel('Total Alcohol Consumption (liters of pure alcohol per capita)', fontsize=10, color='black')
plt.title('Vodka and Total Alcohol Consumption by Region in 2022', fontsize=18, fontweight='bold', color='black')
ax1.tick_params(axis='y', labelcolor='blue')
ax2.tick_params(axis='y', labelcolor='red')

ax1.set_xticks([])
ax1.set_xticklabels([])

x_numeric = np.arange(len(temp_data))
y_1_values = temp_data['Vodka'].values
y_2_values = temp_data['Total alcohol consumption (in liters of pure alcohol per capita)'].values

regression_vodka = MNK(x_numeric, y_1_values)
regression_total_consumption = MNK(x_numeric, y_2_values)

regression_line_1 = regression_vodka[0] * x_numeric + regression_vodka[1]
regression_line_2 = regression_total_consumption[0] * x_numeric + regression_total_consumption[1]

regression_line_1_plot, = ax1.plot(temp_data['Region'], regression_line_1, 'b--', label='Vodka Regression')
regression_line_2_plot, = ax2.plot(temp_data['Region'], regression_line_2, 'r--', label='Total Consumption Regression')

plt.legend(
    handles=[vodka_scatter, total_consumption_scatter, regression_line_1_plot, regression_line_2_plot],
    labels=['Vodka', 'Total Consumption', 'Vodka Regression', 'Total Consumption Regression'],
    loc='upper right',
    fontsize=12,
    frameon=False,
    facecolor='white',
    edgecolor='white',
    labelcolor='black'
)

fig.tight_layout()
plt.show()

sns.set()

fig, ax1 = plt.subplots(figsize=(12, 8))
ax2 = ax1.twinx()

beer_scatter = ax1.scatter(temp_data['Region'], temp_data['Beer'], color='green', label='Beer', edgecolors='black')
total_consumption_scatter = ax2.scatter(temp_data['Region'], temp_data['Total alcohol consumption (in liters of pure alcohol per capita)'], color='red', label='Total Consumption', edgecolors='black')

ax1.set_ylabel('Beer Consumption', fontsize=10, color='black')
ax2.set_ylabel('Total Alcohol Consumption (liters of pure alcohol per capita)', fontsize=10, color='black')
plt.title('Beer and Total Alcohol Consumption by Region in 2022', fontsize=18, fontweight='bold', color='black')
ax1.tick_params(axis='y', labelcolor='green')
ax2.tick_params(axis='y', labelcolor='red')

ax1.set_xticks([])
ax1.set_xticklabels([])

y_1_values = temp_data['Beer'].values

regression_beer = MNK(x_numeric, y_1_values)

regression_line_1 = regression_beer[0] * x_numeric + regression_beer[1]
regression_line_2 = regression_total_consumption[0] * x_numeric + regression_total_consumption[1]

regression_line_1_plot, = ax1.plot(temp_data['Region'], regression_line_1, 'g--', label='Beer Regression')
regression_line_2_plot, = ax2.plot(temp_data['Region'], regression_line_2, 'r--', label='Total Consumption Regression')

plt.legend(
    handles=[beer_scatter, total_consumption_scatter, regression_line_1_plot, regression_line_2_plot],
    labels=['Beer', 'Total Consumption', 'Beer Regression', 'Total Consumption Regression'],
    loc='upper right',
    fontsize=12,
    frameon=False,
    facecolor='white',
    edgecolor='white',
    labelcolor='black'
)

fig.tight_layout()
plt.show()
