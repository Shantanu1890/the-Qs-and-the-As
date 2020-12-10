'''
10

4 5 -2 0 1 -56 9 0 2 0

Sample Output 1:

0.50

0.20

0.30

21
'''
#Code Author : Pranav Viswanathan
n = int(input())
l = input()

myList = l.split()
myList = list(map(lambda x: int(x), myList))
def FunList (n, myList):
    positiveNumber = 0
    negativeNumber = 0
    zeroNumber = 0
    sum1 = 0
    for i in myList:
        if i > 0:
            positiveNumber += 1
            sum1 += i
        elif i < 0:
            negativeNumber += 1
        else:
            zeroNumber += 1
    posFrac = (positiveNumber / n)
    negFrac = (negativeNumber / n)
    zeroFrac = (zeroNumber / n)
    print("{0:.2f}".format(posFrac))
    print("{0:.2f}".format(negFrac))
    print("{0:.2f}".format(zeroFrac))
    print(sum1)
FunList (n, myList)
