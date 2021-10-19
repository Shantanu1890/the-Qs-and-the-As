N=int(input('enter the money stored in his pocket:'))
M=int(input('enter the number of wrappers:'))
C=int(input('enter price of chocolate'))
initial=int(N/C)
free=initial/M
total=int(initial+free)
print("the number of chocolates is =",total)
