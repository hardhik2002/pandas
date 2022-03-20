import pandas as pd 
from line import *
demo_data={
    "cars":["tayota","hundayi","mahindra"], 
    "passings":[2,2,1]
}
print(pd.DataFrame(demo_data))
l()
# sries in pandas
# series is like colum in a table
# or a singe dimensional array
lst_1=[1,2,3,4,5,6,7,8,9,10]
series=pd.Series(lst_1)
print(series)
l()
print("accesing labels")
print(series[0:6])
l()
# we can also create our own named labels
# We need to use index attribute to name our own labels.
# let's try once
x=("Hardhik",38,"CSM","A")
data=pd.Series(x,index=("Name","Roll no.","Branch","Section"))
print(data)
l()

"""
Note: We cannot use set in pandas becuase it won't maintain insertion order

"""
