import pandas as pd
data=[i for i in input("Enter name adress pincode details with spaces:").split()]
final_data=pd.Series(data,index=["Name","Address","Pin code"])
print(final_data)

lst=[]
for i in range(1,21):
    if i%2==0 and i%4==0:
        lst.append(i)
    else:
        pass
print(lst)

lst=["Brazzil","Russia","italy","cuba","soudi"]
user_country=input("Enter the country name:")
if user_country in lst:
    print(user_country," is in BRICS")
else:
    print("Not")

from subprocess import list2cmdline


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
  
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

print(result)

lst=[1,2,2,2,2,3]
lst_=[]
user_input=int(input("Enter a element:"))
for i in range(0,len(lst)):
    if i==user_input:
       
        count=lst.count(i)
        
    elif lst[i]==user_input:
        
        lst_.append(i)
    else:
        pass
print("the count is:",count)
print("the positions are:",lst_)

random_lst=[int(i) for i in input().split()]
even_lst=[]
odd_lst=[]
print(random_lst)
for x in random_lst:
    if x%2==0:
        even_lst.append(x)
    else:
        odd_lst.append(x)
print(even_lst,odd_lst,sep="\n")



random_lst=[int(i) for i in input().split()]
lst=[]
for i in random_lst:
    if i>0:
        lst.append(i)
    else:
        pass
print(tuple(list))


import cmath

a = 1
b = 4
c = 2


dis = (b**2) - (4 * a*c)


ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)


print('The roots are')
print(ans1)
print(ans2)

rows = int(input("Enter the number of rows: "))  
for i in range(0, rows + 1):  
      
    for j in range(rows - i, 0, -1):  
        print(j, end=' ')  
    print()  
        