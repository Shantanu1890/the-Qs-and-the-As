def des(alist):
    n=len(alist)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if alist[j]<alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    return alist

print(des([10,-12,33,15,11,10,-22,0]))

def asc(lis):
    n=len(lis)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis

print(asc([10,-12,33,15,11,10,-22,0]))
