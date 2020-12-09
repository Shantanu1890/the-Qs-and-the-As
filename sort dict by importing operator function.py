import operator
dict1={6:8,8:4,5:6}
print(dict1)
sort=sorted(dict1.items(),key=operator.itemgetter(1))
print('ascending order:',sort)

#use reverse= True for descending order
