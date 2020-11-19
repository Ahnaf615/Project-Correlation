import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('healthdata.csv')
Country = data['Country']
Lifetime = data['Life Expectancy']
PopulationGrowth = data['Population Growth Rate In Percent']
plt.style.use('seaborn')

plt.scatter(Lifetime, PopulationGrowth, color='grey')
plt.xlabel('Life expectancy in years')
plt.ylabel('Population growth rate in percent')
plt.savefig('correlation.png')
plt.show()
