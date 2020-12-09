import math
i=1
while i>0:
    l=int(input())
    w=int(input())
    c=float(w/((4*l*l)+(w*w))**(1/2))
    print(c)
    d=math.asin(c)*180/3.14159
    print(d)
