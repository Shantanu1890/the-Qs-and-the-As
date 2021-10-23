import re
register=input("Enter the register number : ")
if re.match("^[1-9][0-9][A-Za-z][a-zA-Z][a-zA-Z][1-9][0-9][0-9][0-9]",register):
    print("matched")
else:
    print("not matched")
