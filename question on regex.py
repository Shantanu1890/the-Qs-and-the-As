import re
s=input()
flg=False
yu=str(s[0:2])
lis=["KL","TN","MH","DL","OR","GJ","CH","BH","AP","TL","WB","HR","JK"]
if re.match("^[A-Z]{2}\s[1-2][0-9]{3}\s[0]{3}[0-9]{6}",s):
    for i in range(0,len(lis)):
        if yu==str(lis[i]):
            flg=True
            break
if flg==True:
    print("Valid")
else:
    print("Not Valid")
