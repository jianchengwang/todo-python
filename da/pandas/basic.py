from __future__ import print_function
import pandas as pd
import numpy as np

print(pd.__version__)

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
pd.DataFrame({ 'City name': city_names, 'Population': population })

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
# 显示统计信息
# print(california_housing_dataframe.describe())
# 显示前几个
# print(california_housing_dataframe.head())
# 绘制图表
# california_housing_dataframe.hist('housing_median_age')

# access data
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
# print(type(cities['City name']))
# print(cities['City name'])
# print(type(cities['City name'][1]))
# print(cities['City name'][1])

# print(type(cities[0:2]))
# cities[0:2]

# manipulating data
# print(population / 1000)
# np.log(population)

# print(population.apply(lambda val: val > 1000000))

# cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
# cities['Population density'] = cities['Population'] / cities['Area square miles']
# print(cities)

# index
# print(city_names.index)
print(cities)
cities.reindex([0, 1, 2])
print(cities)