from Analysys_Russia.Code.Bartek.Main import russian_data, plt, sns, pd, np

def MNK(x, y):
    x_2 = x ** 2
    A = np.array([[x_2.sum(), x.sum()], [x.sum(), len(x)]])
    B = np.array([(x * y).sum(), y.sum()])
    find = np.linalg.inv(A).dot(B)
    return find

temp_data = russian_data.copy()
temp_data.sort_values(by='Beer', ascending=True, inplace=True)
temp_data = temp_data.dropna()
y_1_values = temp_data['Beer']
y_2_values = temp_data['males ']

x_value = temp_data['Region']

sns.set()

fig, ax1 = plt.subplots(figsize=(10, 8))

ax2 = ax1.twinx()
ax1.scatter(x_value, y_1_values, label='Beer Consumption', color='red')
ax2.scatter(x_value, y_2_values, label='Life Expectancy', color='green')

x_numeric = np.arange(len(x_value))

regression_beer = MNK(x_numeric, y_1_values)
regression_life_expectancy = MNK(x_numeric, y_2_values)

regression_line_1 = regression_beer[0] * x_numeric + regression_beer[1]
ax1.plot(x_value, regression_line_1, 'r--', label='Beer Regression')

regression_line_2 = regression_life_expectancy[0] * x_numeric + regression_life_expectancy[1]
ax2.plot(x_value, regression_line_2, 'g--', label='Life Expectancy Regression')

ax1.set_ylabel('Beer Consumption')
ax2.set_ylabel('Life Expectancy')
ax1.set_xticks(range(len(x_value)))
ax1.set_xticklabels(x_value, rotation=45, ha='right', fontsize=10)

ax2.set_ylim(55, 75)

fig.suptitle('Beer consumption and life expectancy of men in Russian regions')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
fig.subplots_adjust(top=0.9, bottom=0.2)

plt.show()

plt.figure(figsize=(8, 6))

coef = y_2_values / y_1_values
print(coef)

plt.scatter(x_value, coef, marker='o', color='blue', label='Male Life Ex/Beer')

plt.xticks(rotation=45, ha='right', fontsize=12)

plt.subplots_adjust(bottom=0.25, top=0.9)

plt.tick_params(axis='x', pad=10)

regression_coef = MNK(x_numeric, coef)
regression_line_3 = regression_coef[0] * x_numeric + regression_coef[1]
plt.plot(x_value, regression_line_3, '--', label='Coef Regression', color='purple')

plt.title('Dependency of Beer Consumption vs. Male Life Expectancy', fontsize=14)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Life Expectancy / Beer Consumption Ratio', fontsize=12)

plt.ylim(min(coef) - 0.1, max(coef) + 0.1)

plt.legend(loc='upper right')

plt.show()
