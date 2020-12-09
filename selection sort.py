def sel(lis):# selection sorts in ascending order
    n=len(lis)
    for i in range(0,n-1):
        min=i
        sma=lis[i]
        for j in range(i+1,n):
            if lis[j]<lis[min]:
                min=j
                sm=lis[j]
        lis[i],lis[min]=lis[min],lis[i]
    return lis
def inte(lis):# converts str in list to integer
    ctr=0
    for i in lis:
        lis[ctr]=int(i)
        ctr+=1
    return lis
s=input("enter the numbers seperated via a space (" ") : ")
unsor=inte(s.split(" "))
print("the sorted list is : ",sel(unsor))
