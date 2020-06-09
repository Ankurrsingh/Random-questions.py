"""If you want to run this program where input formats are there then only run function part .though u can run whole program independently"
def stringAnagram(dictionary, query):
    l=[]
    for i in range(len(query)):
        count=0
        for j in range(len(dictionary)):
            if(sorted(dictionary[j])== sorted(query[i])):
                count+=1
            else:
                pass
        l.append(count)
        print(l)

n=int(input("enter number of item you want to insert in dictionary"))
m=int(input("enter number of item you want to insert in query"))
dictionary=[]
query=[]
for i in range(n):
    d=str(input("enter items in dictionary"))
    dictionary.append(d)
for i in range (m):
    q=str(input("enter items in query"))
    query.append(q)
stringAnagram(dictionary, query)
