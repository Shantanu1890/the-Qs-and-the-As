def calc(n,st):
    L=st.split(" ")
    i=0
    pos=0
    neg=0
    ze=0
    su=0
    for j in L:
        L[i]=int(j)
        i+=1
    if (i+1)!=n:
        print("invalid")
        exit()
    for i in L:
        if i>0:
            su+=i
            pos+=float(1/n)
        elif i<0:
            neg+=float(1/n)
        else:
            ze+=float(1/n)
    return pos,neg,ze,su
nu=int(input())
s=input()
if nu<=0:
    print("invalid")
    exit()
p,n,z,t=calc(nu,s)
print(round(p,2))
print(round(n,2))
print(round(z,2))
print(t)
