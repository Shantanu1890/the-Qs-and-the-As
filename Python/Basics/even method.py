def even(n):
    x=[]
    for i in n:
        if i%2==0:
            x.append(i)
    return x
print(even([1,2,3,4,5,6,7,8,9,10]))
