n=int(input())
if((n%2==0) or (n<=0)):
    print("invalid input")
    exit
else:
    for i in range(3,8,2):
        x=int(n*i)
        print(x)
