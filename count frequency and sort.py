import collections 
from collections import Counter

def CountFrequency(arr): 
    l=len(arr)
    c=collections.Counter(arr)
    s=[]
    for key, value in c.items():
        if((value/l)>=0.05):
            s.append(key)
        else:
            pass
    s.sort()
    print(s)
    
    
arr=[]
n=int(input("number of elements you want to enter in array"))
for i in range (n):
    a=str(input("enter values"))
    arr.append(a)
CountFrequency(arr)
