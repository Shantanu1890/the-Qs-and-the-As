def lis(se1, se2):
    listi=[]
    for i in se1:
        if i in se2:
            listi.append(i)
    return listi
si=input()
s=input()
print(lis(si,s))
