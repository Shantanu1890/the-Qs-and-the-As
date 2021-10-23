print("enter the number of hours and minutes")
hr=int(input())
mins=int(input())
amt=0
if hr>=7 or mins>59:
    print("invalid input")
elif hr>5:
    amt=200
    hr-=5
    amt+=((hr*50)+(mins*1))
    print("total amount is::",amt)
else :
    amt+=(hr*50+mins*1)
    print("total amount is::",amt)
    
