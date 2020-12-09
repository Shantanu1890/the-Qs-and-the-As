def searc(lis):
    for i in range(0,len(lis)-1):
        ctr=-1
        j=i+1
        if lis[i]>lis[j]:
            ctr=j
            break
    if ctr>-1:
        return len(lis[ctr:])
    else:
        return 0
def inte(lis):# converts str in list to integer
    ctr=0
    for i in lis:
        lis[ctr]=int(i)
        ctr+=1
    return lis
s=input()
unsor=inte(s.split(","))
nu=searc(unsor)
print(nu)
