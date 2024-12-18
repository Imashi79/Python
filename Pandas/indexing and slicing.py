import pandas as pd

#Indexing

data = {"Name": ["Anne","Jane","Tim","Jhone","Micle"],
                   "Age": [10,14,16,13,17],
                   "hobby":["Reading","Dancing","reading","Gardening","Hiking"]}
df = pd.DataFrame(data)
print(df)

#Selecting sigle cloumn
print(df["Name"])
#select multiple column
print(df[["Name","Age"]])
print(df[df['Age'] > 13])  # Filter rows where Age > 13 
print(df[(df['Age']>13) &(df['hobby']=='reading') ])

#1.Label-based Indexing (.loc):Access rows and columns by labels.
df1 = pd.DataFrame(data, index=['a','b','c','d','e'])

print (df1)

print(df1.loc['a']) #access specific row
print(df1.loc[['a','c']]) # access specific rows
#modify specific cell
df1.loc['a','Age']= 18
print (df1)

print(df1.loc['a',"Name"]) #acces specific cell
print(df1.loc[df1['Age']>15]) # check codition 

# 2.Position-based Indexing (.iloc):Access rows and columns by integer position.

print(df1.iloc[0]) #access specific row
print(df1.iloc[[0,3]]) #access mulitiple row
print()
print(df1.iloc[2,2]) #access specific cell
print(df1.iloc[ : ,[1]]) # acess specific column

#Slicing 
  # df.loc[row_start:row_end, column_start:column_end] : inclusive of both start and end labels
  
print(df1.loc['a': 'c'])
print(df1.loc[:'d'])
print(df1.loc['a':'c', 'Age'])
print(df1.loc['a':'c', ['Name','Age']])

# df.iloc[row_start:row_end, col_start:col_end] : exclusive of the end index
print(df1.iloc[:2]) # row 0-2 butnot include 2
print(df1.iloc[-1]) #last row
print(df1.iloc[: , 0]) # sepecific cloum
print(df1.iloc[0:3, :2])

# .iat & .at
print(df1.at['a', 'Name'])  # Access single value by label
print(df1.iat[0, 0])        # Access single value by position

