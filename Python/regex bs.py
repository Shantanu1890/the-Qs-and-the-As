import re
s=input()
if re.match("[5-9]+[5-9]$",s):
    print("valid")
else:
    print("invalid")
