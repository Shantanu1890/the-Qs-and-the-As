
#mean
lis=[1,2,0,9,8,7,5,5]
s=len(lis)
mean=sum(lis)/s
print("mean of the numbers is",mean)
#mean end median begin
lis.sort()
print(lis)
if s%2==0:
    medi1=lis[s//2]
    medi2=lis[s//2 -1]
    median=(medi1+medi2)/2
else:
    median=lis[s//2]
print("median of the numbers is : ",median)
#end of median mode begins
ctr=0
points=[]
for i in range (0,s):
    for j in range (0,s):
        if lis[i]==lis[j]:
            ctr+=1
    points.append(ctr)
    ctr=0
print(points)
pos=0
ctr=0
for k in range(0,s):
    if(points[k]>ctr):
       ctr=lis[k]
       pos=k
print("mode of numbers=",lis[pos])
