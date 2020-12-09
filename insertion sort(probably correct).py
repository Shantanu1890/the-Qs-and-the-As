def inser(lis):# insertion sorts in ascending order
    n=len(lis)
    for i in range(0,n):
        key=lis[i]
        j=i-1
        while j>=0 and key<lis[j]:
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=key
    return lis
def inte(lis):# converts str in list to integer
    ctr=0
    for i in lis:
        lis[ctr]=int(i)
        ctr+=1
    return lis
s=input("enter the numbers seperated via a space (" ") : ")
unsor=inte(s.split(" "))
print("the sorted list is : ",inser(unsor))
