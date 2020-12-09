s=int(input())
temp1=0
temp2=1
if s<=0:
    print("invalid")
elif s==1:
    print(temp1)
elif s==2:
    print(temp1,",",temp2)
else:
    i=0
    print(temp1)
    print(temp2)
    while i<s:
        su=temp1+temp2
        print(su)
        temp1=temp2
        temp2=su
        i+=1

