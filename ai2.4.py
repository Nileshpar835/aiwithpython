#missing values
# methods
# droping missing
# df=df.dropna()
# df=df.dropna(axis=1)#drop column with missing values
import pandas as pd

# filling missing
# df["clumn_name"]=df["column_name"].fillna(0)
#forward
# df.fillna(method="ffill")
#backword
# df.dfillna(method="bfill")

# interpolation
# df["column_name"]=df["column_name"].interpolate()

# data transformation
# renaming
# df=df.rename(columns={"old_name":"new_name"})
# change data types
# df["column_name"]=df["column_name"].astype("float")
# df["column_name"]=pd.to_datetime(df["column_name"])

# create or midify columns

# df["new_column"]=df["existing_column"]*2


# combining and merging dataframes
# concat

# combined=pd.concat(df1,df2,axis=0) columns
# combined=pd.concat(df1,df2,axis=1) rows
# merging


# merged=pd.merge(df1,df2, on="comman_column")
# merged=pd.merge(df1,df2,how="left",on="comman_column")
# merged=pd.merge(df1,df2,how="inner",on="comman_column")
# joining
# joined=df1.join(df2, how="inner")



import pandas as pd
import numpy as np


# create sample dataset

# data={"Names":["nilesh","ritik",np.nan ,"harsh"],
#       "age":[19,np.nan,23,24],
#       "score":[85,86,np.nan,80]
#       }
#
# df=pd.DataFrame(data)
# print("original data:\n",df)
#
# df["age"]=df["age"].fillna(df["age"].mean())
# df["score"]=df["score"].interpolate()
#
# print("new data:\n",df)
#
# df=df.rename(columns={"Names":"Student_Names","score":"Student_Score"})
#
# print("new data:\n",df)
# df1=pd.DataFrame({
#     "Id":[1,2,3],
#     "Name":["nilesh","ritik","kunal"],
#     "age":[25,26,20]
#
# })
# df2 = pd.DataFrame({
#     "Id": [1, 2, 3],
#     "score": [85,20,30],
# })
# print("df1 \n:",df1)
# print("df2 \n:",df2)
# merged=pd.merge(df1,df2,on="Id",how="inner")
# print("merged \n",merged)
# merged["score_percentage"]=(merged["score"]/100)*100
# print("transforemed dataset \n",merged)

# Step 1: Create 3 sample DataFrames
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, None, 30],
    'city': ['NY', 'LA', 'NY']
})

df2 = pd.DataFrame({
    'id': [1, 2, 3],
    'salary': [50000, 60000, None],
    'department': ['HR', 'IT', 'IT']
})

df3 = pd.DataFrame({
    'id': [1, 2, 3],
    'experience': [2, 5, None],
    'bonus': [1000, 2000, 3000]
})

# Step 2: Drop columns with more than 50% missing values
for df in [df1, df2, df3]:
    df.dropna(thresh=len(df)*0.5, axis=1, inplace=True)

# Step 3: Merge all three datasets on 'id'
merged_df = df1.merge(df2, on='id').merge(df3, on='id')

# Step 4: One-hot encode categorical columns
final_df = pd.get_dummies(merged_df)

# Show the final result
print("Final Processed DataFrame:\n")
print(final_df)
