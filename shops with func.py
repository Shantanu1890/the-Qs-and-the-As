def func(i,inv,ct):
    if ct==len(inv):
        return
    temp=inv[i]
    cost,stock=temp[0],temp[1]
    tot=cost*stock
    print(i)
    print('%.2f'%tot)

inventory={}
add=0
ctr=0
stonks=0
refer=["shoes","socks","belts","shiners","bags"]
s=int(input())
for i in range(0,s):
    item=input()
    icost=float(input())
    istock=int(input())
    inventory[item]=(icost,istock)
    add=add+(icost*istock)
    stonks+=istock
for i in refer:
    func(i,inventory,ctr)
    ctr+=1
    if ctr==len(inventory):
        break
print(stonks)
print('%.2f'%add)
