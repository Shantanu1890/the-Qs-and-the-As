fo=open("F:\\random\\hello.txt","w+")#w,r,a,r+,rb
#print(fo.write("hey yall scott here"))
print("Name of the file : ",fo.name)
print("Is file closed ? : ",fo.closed)
print("Opening mode : ",fo.mode)
fo.writelines(["hello"," World"])
fo.close

#r+ is read + write
#a is append
#w+ is writing + reading
