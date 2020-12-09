import re
s=input("Enter the PAN Number : ")
if re.match("^[A-Za-z][a-zA-Z][A-Za-z][a-zA-Z][A-Za-z][0-9][0-9][0-9][0-9][A-Za-z]",s):
    print("matched")
else:
    print("not matched")
