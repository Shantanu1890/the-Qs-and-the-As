A=[("A",1),("B",2),("C",3)]
dict1=dict()
for i,j in A:
    dict1.setdefault(i,j)
print(dict1)
