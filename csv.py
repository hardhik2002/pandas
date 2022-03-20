import pandas as pd
df=pd.read_csv("data.csv")
print(df.to_string())
n1,atm=map(float,input().split())

if n1%5==0 and n1<=atm:
    print(atm-n1)
else:
    print(atm)
