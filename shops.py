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
    if ctr==len(inventory):
        break
    tempVal=inventory[i]
    cost,stock=tempVal[0],tempVal[1]
    tot=cost*stock
    print(i)
    print('%.2f'%tot)
    ctr+=1
print(stonks)
print('%.2f'%add)
