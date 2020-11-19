import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('healthdata.csv')
Country = data['Country']
Lifetime = data['Life Expectancy']
PopulationGrowth = data['Population Growth Rate In Percent']
plt.style.use('seaborn')

plt.scatter(PopulationGrowth, Lifetime, color='grey')
plt.xlabel('Population growth rate in percent')
plt.ylabel('Life expectancy in years')
plt.title('Correlation done by Ahnaf Khan')
plt.savefig('correlation.png')
plt.show()
