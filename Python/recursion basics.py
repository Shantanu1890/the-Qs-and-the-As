#recursion

def fun(n):
    print(n)# base case
    if n>1:
        return fun(n-1)# recursive case
fun(int(input()))


def fak(n):
    if n>1:
        return (n*fak(n-1))
    else:
        return 1
print(fak(int(input())))
