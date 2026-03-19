import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data=pd.read_csv("house_prices.csv")

x= data[['size','rooms']]
y= data['price']

X_train, X_test,y_train, y_test = train_test_split(x,y,test_size=0.2)

model = LinearRegression
model.fit(X_train,y_train)

prediction = model.predict(X_test)

error = mean_absolute_error(y_test,prediction)

print("mean Squared Error",error)