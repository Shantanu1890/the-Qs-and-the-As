i=1
while i>0:
    l=int(input("lambda  "))
    n=int(input("diff order  "))
    d=int(input("d value  "))
    r=float(input("radius of ring  "))
    tot=float((1.22)*(l)*(n)*(d/r))*(10**(-3))
    print("Ans= ",tot)
