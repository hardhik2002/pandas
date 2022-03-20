import pandas as pd
from line import *
"""
DataFrame is a 2 dimensional data structure
like a two dimensional array, or a table with rows and colums.
"""
data={
    "Names":["Hardhik","Haneesha","Hampika"],
    "GPA":[8.8,8.7,9.0]
}
data_frame=pd.DataFrame(data)
print(data_frame)
l()
# manuculating indexes
data_frame=pd.DataFrame(data,index=[1,2,3])
print(data_frame)
l()
# Locating row
print(data_frame.loc[1])
'''
Note:This example returns panda series
'''
l()
print(data_frame.loc[[1,2]])
l()
'''
Note: When using [], the result is pandas DataFrame
'''



