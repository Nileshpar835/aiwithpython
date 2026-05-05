import pandas as pd

housing = pd.read_csv('housing.csv')
print(housing.head())
housing.describe()

housing["ocean_proximity"].value_counts()

import matplotlib.pyplot as plt

housing.hist(bins = 50 , figsize=(20,15))

plt.show()


#data cleaning 

fltr_idx = housing['total_bedrooms'].notna() & (housing['housing_median_age'] < 52) & (housing['median_house_value'] < 500001)

fltr_housing = housing[fltr_idx].reset_index(drop=True)

fltr_housing.head()

fltr_housing.info()

fltr_housing.describe()

fltr_housing.hist(bins = 50 , figsize = (15,10))

plt.show()


from sklearn.preprocessing import OneHotEncoder

encoded_cat, categories = fltr_housing["ocean_proximity"].factorize() # retrieve the attribute encoded as numbers
encoded_cat_arr = OneHotEncoder().fit_transform(encoded_cat.reshape(-1,1)).toarray() # transform sparse matrix to NumPy array
enc_fltr_housing = fltr_housing.iloc[:,0:9].copy()
for i in range(0, len(categories)):
    enc_fltr_housing[categories[i]] = encoded_cat_arr[:,i]
enc_fltr_housing.head()

import numpy

rnd_indices = numpy.random.permutation(len(enc_fltr_housing)) # Generate a random sequence of housing's index
test_set_size = int(len(enc_fltr_housing) * 0.2) 
print(test_set_size, " datapoints for test set")

test_indices = rnd_indices[:test_set_size]
train_indices = rnd_indices[test_set_size:]
print(test_indices, " ", len(test_indices))
print(train_indices, " ", len(train_indices))

test_set1 = enc_fltr_housing.iloc[test_indices].reset_index(drop=True) # Pick data out of housing according to the test indices
test_set1.head()

train_set1 = enc_fltr_housing.iloc[train_indices].reset_index(drop=True)
train_set1.head()

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

lnr_regressor1 = LinearRegression()
lnr_regressor1.fit(train_set1.iloc[:, [idx for idx in range(len(train_set1.columns)) if idx != 8]], train_set1['median_house_value'])
prediction1 = lnr_regressor1.predict(test_set1.iloc[:, [idx for idx in range(len(test_set1.columns)) if idx != 8]])
print('RMSE = ', numpy.sqrt(mean_squared_error(test_set1['median_house_value'], prediction1)))


train_set2 = train_set1.copy()
train_set2['room_per_house'] = train_set2['total_rooms']/train_set2['households']
train_set2['bedroom_per_room'] = train_set2['total_bedrooms']/train_set2['total_rooms']
train_set2['pop_per_house'] = train_set2['population']/train_set2['households']
train_set2.head()

test_set2 = test_set1.copy()
test_set2['room_per_house'] = test_set2['total_rooms']/test_set2['households']
test_set2['bedroom_per_room'] = test_set2['total_bedrooms']/test_set2['total_rooms']
test_set2['pop_per_house'] = test_set2['population']/test_set2['households']
test_set2.head()

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

lnr_regressor2 = LinearRegression()
lnr_regressor2.fit(train_set2.iloc[:, [idx for idx in range(len(train_set2.columns)) if idx != 8]], train_set2['median_house_value'])
prediction2 = lnr_regressor2.predict(test_set2.iloc[:, [idx for idx in range(len(test_set2.columns)) if idx != 8]])
print('RMSE = ', numpy.sqrt(mean_squared_error(test_set2['median_house_value'], prediction2)))

from sklearn.ensemble import RandomForestRegressor

frst_regressor1 = RandomForestRegressor()
frst_regressor1.fit(train_set1.iloc[:, [idx for idx in range(len(train_set1.columns)) if idx != 8]], train_set1['median_house_value'])
prediction3 = frst_regressor1.predict(test_set1.iloc[:, [idx for idx in range(len(test_set1.columns)) if idx != 8]])
print('RMSE = ', numpy.sqrt(mean_squared_error(test_set1['median_house_value'], prediction3)))

from sklearn.ensemble import RandomForestRegressor

frst_regressor2 = RandomForestRegressor()
frst_regressor2.fit(train_set2.iloc[:, [idx for idx in range(len(train_set2.columns)) if idx != 8]], train_set2['median_house_value'])
prediction4 = frst_regressor2.predict(test_set2.iloc[:, [idx for idx in range(len(test_set2.columns)) if idx != 8]])
print('RMSE = ', numpy.sqrt(mean_squared_error(test_set2['median_house_value'], prediction4)))


