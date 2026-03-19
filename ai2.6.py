import matplotlib.pyplot as plt

# bar chart

# categories=["A","B","C"]
# values=[10,25,39]
#
# plt.bar(categories,values,color="red")
# plt.title("Bar Chart")
# plt.show()

#histogram
# data=[1,2,3,4,5,1,21,4,4,2,2,1]
# plt.hist(data,bins=4,color='red',edgecolor='black')
# plt.title('Histogram of data')
# plt.show()
#


# scatter plot
# x=[1,2,3,4,5]
# y=[10,12,25,30,45]
#
# plt.scatter(x,y,color="blue")
# plt.title("Scatter Plot")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend(["x"])
# plt.show()


# customizing plots
# title,legend,axis


#basic plot
# x=[1,2,3,4,5]
# y=[10,25,10,15,30]
#
# plt.plot(x,y)
# plt.show()
#

# types
# line plot
# plt.plot([1,2,3],[4,5,6],label="trends",color="orange",linestyle="--",marker="x")
# plt.title("Line plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend()
# plt.show()

# seaborn
# heatmap
import seaborn as sns
import numpy as np
#
# data=np.random.rand(5,5)
# sns.heatmap(data, annot=True,cmap="coolwarm")
# plt.title("Heatmap")
# plt.show()
# pairplot


# line plot
# years=[2010,2011,2012,2013,2014]
# sales=[100,120,140,145,180]
# plt.plot(years,sales,label="sales",color='red',marker='o')
# plt.title('sales vs years')
# plt.xlabel('years')
# plt.ylabel('sales')
# plt.legend()
# plt.show()
#
# plt.scatter(years,sales,label="sales",color='red',marker='o')
# plt.title('sales vs years')
# plt.xlabel('years')
# plt.ylabel('sales')
# plt.show()
#
# import pandas as pd
# # load datase
# df=pd.read_csv("iris.csv")
#
# del df["species"]
# # cal correlaiton matrix
# corre=df.corr()
#
# # plot heatmap
# sns.heatmap(corre,annot=True,cmap="coolwarm")
# plt.title("Iris Dataset")
# plt.show()



# bar chart
#
# categories=["electronics","clothing","groceries"]
# revenue=[250,400,450]
# plt.bar(categories,revenue,color='blue',edgecolor='black')
# plt.title('revenue')
# plt.show()
