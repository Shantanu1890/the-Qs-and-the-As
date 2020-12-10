'''
Write a recursive function that, given two strings/integers/alphanumeric, returns whether the first string
is a subsequence of the second. 

For example, please check the sample input and outputs. If the inputs contain a integer and a string, print as invalid.

Input Format:

In the first line, enter the first string/integer

In the second line, enter the second string/integer

Output Format:

In the first line, enter yes if the first string is a substring of the second else print no/invalid.

Sample Input 1:

har

cathactic

Sample Output 1:

true

Sample Input 2:

2470

1234578

Sample Output 2:

false
'''
#Code Author : Pranav Viswanathan
def isSubSequence(string1, string2, m, n): 
    
    
    if m == 0:    
        return True
    if n == 0:    
        return False
  
    
    if string1[m-1] == string2[n-1]: 
        return isSubSequence(string1, string2, m-1, n-1) 
  
    
    return isSubSequence(string1, string2, m, n-1) 


string1, string2 = "123", "Cathartic"
if ((string1.isalpha() == True) and (string2.isdigit() == True)) or ((string1.isdigit() == True) and (string2.isalpha() == True)):
    print('invalid')
    exit(0)
m = len(string1) 
n = len(string2)

if isSubSequence(string1, string2, m, n): 
    print("yes")
else:
    print('no')
