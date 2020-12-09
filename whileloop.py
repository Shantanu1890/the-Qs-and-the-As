#write a python code to find sum of n natural numbers\

n=int(input("Enter the value"))
total=0
value=1
while(value<=n):
    total+=value
    value+=1
print(total)
