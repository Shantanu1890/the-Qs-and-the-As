def bub(lis):# bubble sorts in ascending order
    n=len(lis)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis
def inte(lis):# converts str in list to integer
    ctr=0
    for i in lis:
        lis[ctr]=int(i)
        ctr+=1
    return lis
s=input("enter the numbers seperated via a space (" ") : ")
unsor=inte(s.split(" "))
print("the sorted list is : ",bub(unsor))
