def pr(a,b=9,*c):
    return a+b+c[0]
def pri(*a,c=9,b=1):
    return a[3]+c+b

print(pri(1,2,4,4,5,6,7))
