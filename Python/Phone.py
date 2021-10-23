import re
s=input("Enter the mobile number : ")
if re.match("^[1-9][0-9]{9}",s):
      print("Number Matched")
else:
    print("Number Not Matched")
