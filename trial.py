n=int(input())
lis=[]
lis2=[]
lis3=[]
c=0
teml=[]
ctr=[]
pos=[]
strg=""
for i in range(0,n):
    temp=input()
    temp2=temp[2:]
    lis.append(set(temp2.split(" ")))

for i in lis:
    for j in i:
        print(j)
        if int(j)<=0:
            print("invalid input")
            exit()




for i in range(0,len(lis)):
    for j in range(0,len(lis)):
        if j>i:
            lis2.append(lis[i].intersection(lis[j]))
            lis3.append(str(str(i+1)+" "+str(j+1)))

if lis2==[set()]:
    lis2=[]

if len(lis2)!=0:
    for i in range(0,len(lis2)):
        ctr.append(len(lis2[i]))
        pos.append(i)

    for i in range(0,len(ctr)):
        if len(lis2[i])==max(ctr):
            for j in lis3[i]:
                strg+=j
            print(strg)#
            strg=""
            for j in lis2[i]:
                teml.append(int(j))
            teml.sort()
            for j in teml:
                strg=strg+str(j)+" "
            print(strg.strip())#
    print(max(ctr))#
else:
    print("no winners")
