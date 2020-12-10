'''
Write a Python program to find the greatest common divisor (gcd) of two integers using recursion. If you have a 
gcd for the two integers, print the gcd. If any one of the integer is 0, print no. If only one integer is given, 
print as invalid.

Input Format:

In the first line get the two integers with a space in between.

Output Format:

Print the gcd else print no or invalid.

Sample Input 1:

36 60

Sample Output 1:

12

Sample Input 2:

3 7

Sample Output 2:

1
'''
#Code Author : Pranav Viswanathan
 def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

nums = input()
l = nums.split()
l = list(map(lambda x: int(x), l))

if len(l) == 1:
    print('invalid')
    exit(0)
elif l[0] == 0 or l[1] == 0:
    print('no')
    exit(0)
else:
    result = GCD(l[0], l[1])
    print(result)
