def f():
    a=3
    def ff():
        print(a)
    return ff
result=f()
result()
