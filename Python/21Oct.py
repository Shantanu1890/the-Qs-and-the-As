import re   # +=at least one occurance of, *=0 or more  ?=0 or 1
s=input("Enter the mobile number : ")
if re.match('^\-[1-9][0-9]*\.?[0-9]*$',s):
      print("Number Matched")
else:
    print("Number Not Matched")
