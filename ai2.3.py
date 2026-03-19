import pandas as pd
#data frame with dictonary

# s=pd.Series([10,20,30],index=["a","b","c"])
# print(s)

# data={"name":["nilesh","ritik"],"age":[21,22]}
# df=pd.DataFrame(data)
# print(df)


# df=pd.read_csv("data.csv")
# df.to_csv("data.csv",index=False)


# df=pd.read_csv("data.xlsx")
# df.to_excel("data.xlsx")


#viewing data
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())

#selecting
# print(df[["name","age"]])

#filter
# print(df[df["age"]>18])

#selecting from perticular position
# print(df.iloc[0])
# print(df.iloc[:,0])

#selecting by label
# print(df.iloc[0])
# print(df.iloc[:,"name"])

# load the dataset
df=pd.read_csv("iris.csv")
#frist 5 rows
# print("First 5 rows:\n",df.head())
# print("last 5 rows:\n",df.tail())

# print(df.info())
# print(df.describe())

selected_column=df[["species","sepal_length"]]
# print("selected column\n",selected_column)

filter_rows=df[(df["sepal_length"]>5.0)& (df["species"]=="setosa") & (df["petal_length"]>1.0)]
# print("filtered row\n",filter_rows)








