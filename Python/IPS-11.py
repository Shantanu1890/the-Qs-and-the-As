'''
Given three points or length of three sides, write an algorithm and the subsequent Python code to check if they can 
form a triangle or not.

Three points can form a triangle if they do not fall in a straight line. Secondly, if the sum of the length of any 
two sides is less than the length of the third sides then they cannot form a triangle.

Use a function coordinate_check(p1, p2, p3) which returns true if all the three points do not lie on a straight line 
else returns false.

Call another function named side_check(s1, s2, s3) which returns true if the sum of the length of any two sides is 
greater than the length of the third sides else returns false.

If the user is given the option to choose either coordinate entries or side length entry for a triangle to check if a 
triangle is possible or not, then your code should return ‘Possible’ or ‘Not Possible’ based on the above-mentioned 
conditions.

Input format:

In the first line, enter 1 if coordinates are to be entered else 2 if side lengths are to be entered. Any other entry
must print ‘Invalid Entry’ and should not proceed further

In the second line, space-separated x-coordinate and y-coordinate of point-1 or length of side-1

In the third line, space-separated x-coordinate and y-coordinate of point-2 or length of side-2

In the fourth line, space-separated x-coordinate and y-coordinate of point-3 or length of side-3

Output format:

Possible, Not Possible, or Invalid Entry

Sample Input 1:

1

2 4

-1 2

0 0

Sample Output 1:

Possible

Sample Input 2:

1

0 0

1 1

-1 -1

Sample Output 2:

Not Possible

Sample Input 3:

2

5

8

10

Sample Output 3:

Possible

Sample Input 4:

2

5

8

20

Sample Output 4:

Not Possible

Sample Input 5:

3

Sample Output 5:

Invalid Entry
'''
#Code Author : Pranav Viswanathan.
def coordinate_check(p1, p2, p3):
    p1Points = p1.split()
    p2Points = p2.split()
    p3Points = p3.split()
    print(p1Points)
    print(p2Points)
    print(p3Points)
    
    slope1 = (((int(p2Points[1]) - int(p1Points[1])) / (int(p2Points[0]) - int(p1Points[0]))))
    slope2 = (((int(p3Points[1]) - int(p2Points[1])) / (int(p3Points[0]) - int(p2Points[0]))))
    
    if slope1 == slope2:
        return False
    else:
        return True
    

def side_check(s1, s2, s3):
    flag = False
    if (s2 + s3) > s1 and (s1 + s3) > s2 and (s1 + s2) > s3 :
        flag = True
    return flag

choice = int(input("1. Co-rdinates\n2. Sides\n[1 \ 2] : "))
if choice == 1:
    p1 = input('p1 : ')
    p2 = input('p2 : ')
    p3 = input('p3 : ')
    if coordinate_check(p1, p2, p3):
        print('Not Possible')
    else:
        print('Possible')
    
elif choice == 2:
    s1 = int(input('s1 : '))
    s2 = int(input('s2 : '))
    s3 = int(input('s3 : '))
    if side_check(s1, s2, s3):
        print('Possible')
    else:
        print('Not Possible')
else:
    print('Invalid Entry')
