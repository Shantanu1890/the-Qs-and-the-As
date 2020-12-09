import re
s=input()
flg1=False
flg2=False
if re.match("^[A-Za-z][0-9A-Za-z]{10,12}",s):
    for i in s:
        if str(i).isdigit():
            flg1=True
        
elif re.match("^[0-9][0-9a-z]{6,9}",s):
    flg2=True
if flg1==True:
    print("valid and strong")
elif flg2==True:
    print("valid and weak")
else:
    print("invalid")
