import pandas as pd


# group=df.groupby("col_name")

# operations
# for name,group in grouped:
    # print(name,group)

# grouped.mean()
# grouped.sum()

# df.groupby("category_col")["numeric_col"].mean()
# df.groupby("cat_col").agg({"numeric_col":["mean","max","min"]})

# pivot_table
# pivot=df.pivot_table(
#     values="numeric_col"
#     ,index="cate_col",
#     aggfunc="mean"
# )

# custom aggregation
# def range_function(x):
#     return x.max() - x.min()

# df.groupby("cate_col")["numeric_col"].agg(range_function)

# df.groupby("cate_col")["numeric_col"].mean()
# df.groupby("cate_col")["numeric_col"].max()
# df.groupby("cate_col")["numeric_col"].min()

# df.groupby("cate_col").agg({"numeric_col":["mean","max","min"]})

# data={
#     "class":["A","B","C","A","C","B"],
#     "score":[10,20,30,40,50,60]
#     ,"age":[15,20,30,32,12,20]
#
#
# }
#
# df=pd.DataFrame(data)
#
# print("original Dataset \n",df)
#
# grouped=df.groupby("class").mean()
# print(grouped)
# stats=df.groupby("class").agg({"score":["mean","max","min"],"age":["mean","max","min"]})
# print(stats)












