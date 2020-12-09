maths=set()
phys=set()
chem=set()
cts=set()
mathn=int(input())
for i in range(0,mathn):
    x=input()
    maths=maths|{x}
    
physn=int(input())
for i in range(0,physn):
    x=input()
    phys=phys|{x}

chemn=int(input())
for i in range(0,chemn):
    x=input()
    chem=chem|{x}

ctsn=int(input())
for i in range(0,chemn):
    x=input()
    cts=cts|{x}
fail=maths|phys|chem|cts
leng=len(fail)
print(leng)
