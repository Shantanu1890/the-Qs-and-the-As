x=int(input("enter the number"))
ctr=0
n=2
while n<x:
    if x%2==0 :
        ctr+=1
    n+=1
if ctr>0:
    print("entered value is a prime number")
else:
    print("entered value is not a prime number")
