'''
Ritika and John has developed a software containing python programs for the satellite application for “Chandrayaan-2” which
will be invoked when it landed in moon on September 7, 2019. They have stored this software in their computer machine which needs to be secured heavily. 
They would like to create a password for their machine. To create this, they came up with the following requirements:
A strong password is the one which:
- should be 11-13 characters long

- it should be alphanumeric(containing alphabets and digits)

Weak Passwords:
-it starts with a digit.

-contains 7 – 10 characters

-contains only lower case letters

If it is a valid password, print whether “Valid and Strong” or “Valid and Weak”. 
If the password does not fall into any of these categories, then print as “invalid”.
In the first line get the password as input.
In the second line print whether it is valid or invalid.
'''
#Code Author : Pranav Viswanathan
import re
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
userPass = '34ACX783@b'
def checkIfFits(x):
    cntA = 0
    cntN = 0
    for i in x:
        if (i.isalpha()):
            cntA = cntA + 1
        elif (i.isnumeric()):
            cntN = cntN + 1
    if(cntA > 0 and cntN > 0):
        if x.islower():
            return False
        else:
            return True
            

def strongPasswordSize(x):
    if 11 <= len(x) <= 13:
        return True
    else:
        return False


def weakPasswordSize(x):
    if 7 <= len(x) <= 10 and x[0].isnumeric() :
        return True
    else:
        return False
        

if checkIfFits(userPass) == True:
    print('1')
    if strongPasswordSize(userPass) == True:
        print('2')
        print("Valid and Strong")
    else:
        print('3')
        print("invalid")
elif checkIfFits(userPass) == False:
    print('4')
    if weakPasswordSize(userPass) == True:
        print('5')
        print("Valid and Weak")
    else:
        print('6')
        print("invalid")
else:
    print('7')
    print("invalid")
