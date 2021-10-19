s=input()
flg1=False
flg2=True
if str(s[0:2])=="KL"or"TN"or"MH"or"DL"or"OR"or"GJ"or"CH"or"BH"or"AP"or"TL"or"WB"or"HR"or"JK" :
    if (s[4].isspace())and(s[9].isspace())and(int(s[5])!=0):
        if(str(s[10:13])=="000")and(len(s)==17)and(str(s[2:4]).isdigit()):
            flg1=True
for i in range(13,17):
    if not str(s[i]).isdigit():
        flg2=False
if (flg1==True)and(flg2==True):                    
    print("valid")
else:
    print("invalid")
