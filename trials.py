def coordinate_check(p1,p2,p3):
    L1=p1.split(" ")
    L2=p2.split(" ")
    L3=p3.split(" ")
    L1[:]=list(map(int,L1))
    L2[:]=list(map(int,L2))
    L3[:]=list(map(int,L3))
    det=L1[0]*(L2[1]-L3[1])-L1[1]*(L2[0]-L3[0])+L2[0]*L3[1]-L2[1]*L3[0]
    if det==0:
        return False
    else:
        return True
def side_check(s1,s2,s3):
    if s1+s2>s3 and s2+s3>s1 and s3+s1>s2:
        return True
    else:
        return False
s=int(input())
if s==1:
    po1=input()
    po2=input()
    po3=input()
    if coordinate_check(po1,po2,po3):
        print("Possible")
    else:
        print("Not Possible")
elif s==2:
    po1=int(input())
    po2=int(input())
    po3=int(input())
    if side_check(po1,po2,po3):
        print("Possible")
    else:
        print("Not Possible")
else:
    print("Invalid Entry")
