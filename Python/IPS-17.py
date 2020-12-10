'''
Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in 
a hyphen-separated sequence after sorting them alphabetically.

Do not use any predefined function for sorting. Print ‘Invalid Entry’ if the entry is anything other than 
alphabets or hyphen. If the entry word has upper case alphabet, then change it to lower case, then sort and 
print the output in lower case.

Sample Input 1:

green-Red-yellow-Black-white
Sample Output 1:

black-green-red-white-yellow

 Sample Input 2: green@Red^yellow%Black+white
Sample Output 2: Invalid Entry
'''
#Code Author : Pranav Viswanathan
import re
string = input()
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')   
if(regex.search(string) != None): 
    print("Invalid")  
string = string.lower()
s = string.split('-')
print(s)
n = len(s) 
for i in range(n): 
     for j in range(0, n-i-1): 
        if s[j] > s[j+1] : 
            s[j], s[j+1] = s[j+1], s[j] 
print(s)
print('-'.join(s))
