def funk(n1,n2):
    if n1<n2:
        return funk(n2,n1)
    elif n2==0:
        return n1
    else:
        return funk(n2,n1%n2)
st=input()
L=st.split(" ")
i=0
for j in L:
    L[i]=int(j)
    i+=1
    if int(j)<=0:
        print("no")
        exit()
if len(L)!=2:
    print("invalid")
    exit()
print(funk(L[0],L[1]))
