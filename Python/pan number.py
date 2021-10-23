pan =input("Enter pan")
flag=False


if len(pan)!=10:
    flag= True
else:
    for i in range(0,5):
        if not pan[i].isupper():
            flag = True
            break
    for i in range(5,9):
        if not pan[i].isdigit():
            flag= True
    if not pan[9].isupper():
        flag = True
if flag ==True:
    print("Invalid")
