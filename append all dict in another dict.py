dict1={'hi':1,'bye':2}
dict2={5:2,6:4}
dict3={1:'x',3:'y'}

dict4={}
for d in (dict1,dict2,dict3):
    dict4.update(d)
print(dict4)
    
