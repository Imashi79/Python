# Creating Series and Dataframes
import pandas as pd

#basic method to create a Series
sc3 = pd.Series([1,4,5,6,7], index= ['A','B','C','D','E'])
print(sc3)

#1. Using a List
list1 = [1,2,3,4,5,6]
sc = pd.Series(list1)
print(sc)

#2. using tuple
tuple1 = (1,2,3,4,5,6)
sc1 = pd.Series(tuple1)
print(sc1)

#3.using Dictionary
dic = {'a':1, 'b':3, 'c':4, 'e':5}
sc2 = pd.Series(dic)
print(sc2)

# use custom index
index = ['a','b', 'c', 'd', 'e', 'f']
sc= pd.Series(list1, index=index)
print (sc)
sc1 = pd.Series(tuple1, index=index)
print(sc1)

#creating basic Data Frame
Dt1 = pd.DataFrame ([{"name": "Anne", "Age": 10},{"name":"John", "Age":11},{"name":"Tim", "Age":12}])
print(Dt1)

Dt2 = pd.DataFrame({"Letters":["a","b","c","d"],
                    "Numbers":[1,2,3,4],
                    "Symbols":['!','@','#','$']})
print (Dt2)

import numpy as np

data = np.array([["Alice", 25, "New York"],
                 ["Bob", 30, "Los Angeles"],
                 ["Charlie", 35, "Chicago"]])
Dt3 = pd.DataFrame(data, columns=["Name", "Age", "City"])
print(Dt3)