import re
s=input()
p=""
temp=""
UwU=[]
ctr=0
for i in s:
    if re.match("^[!@#$%><'?<>\-\"\*\_=:;,\^\+]",str(i)):
        p=p+"."
    elif (ord(i)>=65) and (ord(i)<=90):
        p=p+chr(ord(i)+32)
    else:
        p+=i
for i in p:
    if (str(i)==temp) and (str(i).isalpha()):
        UwU.append(temp+i)
        temp=i
        ctr+=1
    else:
        temp=i
for i in range (0,len(UwU)):
    print(UwU[i],"\n")
print(ctr)
