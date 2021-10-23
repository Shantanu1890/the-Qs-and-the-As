def linear(lis,chk):#searches for the number in the given list
    for i in range(0,len(lis)):
        if lis[i]==chk:
            return True,i
    return False,-1

def inte(lis):# converts str in list to integer
    ctr=0
    for i in lis:
        lis[ctr]=int(i)
        ctr+=1
    return lis
s=input("enter the numbers seperated via a space (\" \") : ")
unsor=inte(s.split(" "))
ch=int(input("Enter the number to be searched : "))
flg,pos=linear(unsor,ch)
if flg:
    print("element ",ch," is present at ",pos," position")
else:
    print("Sorry, Element ",ch," is not present ")
    



#For displaying all positions of the chosen number
def linear2(lis,chk):
    lis2=[]
    for i in range(0,len(lis)):
        if lis[i]==chk:
            lis2.append(i)
    if lis2==[]:
        lis2=Null
    return lis2

    
