'''
Sorting_Asc_Dsc
Given a list of integers, arrange them in an order such that all the even numbers are placed first in 
descending order and then the odd numbers are placed in ascending order. The integers include repeated numbers also.

Input format:

In the first line, enter the number of integers in the list.

In the second line, enter space-separated integers in a single line.

Output format:

Display the sorted integers in a single line separated by space.

 

Sample Input 1:

8

10 -12 33 15 11 10 -22 0

Sample Output 1:

10 10 0 -12 -22 11 15 33

 

Sample Input 2:

5

-11 -12 -13 -14 -15

Sample Output 2:

-12 -14 -15 -13 -11


'''
#Code Author : Pranav Viswanathan
n = 5
l = '-11 -12 -13 -14 -15'
myList = l.split()
myList = list(map(lambda x:int(x), myList))
oList =[]
eList = []
for i in myList:
    if i%2==0:
        eList.append(i)
    else:
        oList.append(i)
eList.sort(reverse=True)
oList.sort()
fin = eList + oList
for i in fin:
    print(i, end = ' ')
