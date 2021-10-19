def asc(lis):
    n=len(lis)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis

def des(alist):
    n=len(alist)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if alist[j]<alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    return alist

def inte(lis):# converts str in list to integer
    ctr=0
    for i in lis:
        lis[ctr]=int(i)
        ctr+=1
    return lis

q=int(input())
s=input()
lise=[]
liso=[]
strlis=s.split(" ")
unsor=inte(strlis)
print(unsor)
for i in unsor:
    if i%2==0:
        lise.append(i)
    else:
        liso.append(i)
lise=des(lise)
liso=asc(liso)
unsor=[]
for i in lise:
    unsor.append(i)
for i in liso:
    unsor.append(i)
print(unsor)
