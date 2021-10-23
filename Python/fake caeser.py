stri=input("enter the word: ")
d=list(stri)
r=""
for i in range(0,len(stri)):
    if ord(d[i])>=120:
        d[i]=chr(ord(d[i])-23)
    else:
        d[i]=chr(ord(d[i])+3)
    r=r+d[i]
print(d)
