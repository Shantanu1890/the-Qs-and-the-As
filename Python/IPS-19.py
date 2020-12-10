'''
Searching_Rotate
Given a circular sorted array of integers, find the number of times the array is rotated. Assume that there are 
no duplicate elements in the array and that the array is rotated only in the anti-clockwise direction.

Input format:

In the first line, enter the integers separated by a comma.

Output format:

Display the number of times the list is rotated

 

Sample Input 1:

8,9,10,2,5,6

Sample Output 1:

3

Sample Input 2:

2,5,6,8,9,10

Sample Output 2:

0
'''
#Code Author : Pranav Viswanathan
l = input()
myList = l.split(',')
myList = list(map(lambda x: int(x), myList))
requiredElement = min(myList)
for i in range(len(myList)):
    if myList[i] == requiredElement:
        print(i)
