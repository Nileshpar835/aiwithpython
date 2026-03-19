# #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#
df=pd.read_csv("titanic.csv")
# # print(df.head())
# print(df.info())
# print(df.describe())
#
# # handle missing values
# df["Age"]=df["Age"].fillna(df["Age"].median())
# df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
#
# # remove duplicate
# df=df.drop_duplicates()
#
#
# # filter data:passengers in first class
# first_class=df[df["Pclass"]==1]
# print("First class passenges \n",first_class)
#
# #bar chart survival rate by class
# survivalbt_class=df.groupby("Pclass")["Survived"].mean()
# survivalbt_class.plot(kind="bar",color="skyblue")
# plt.title("Survival vs Pclass")
# plt.ylabel("Pclass")
# plt.show()
#
# # histogram
# sns.histplot(df["Age"],kde=True,bins=20,color="blue")
# plt.title("Age vs Pclass")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()
#
import matplotlib.pyplot as plt

# plt.scatter(df["Age"],df["Fare"],alpha=0.5,color="green")
# plt.title("Age vs Fare")
# plt.xlabel("Age")
# plt.ylabel("Fare")
# plt.show()

