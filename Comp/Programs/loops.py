x = 10
def foo():
    x=3
    bar()
    print x+5

def bar():
    print x+2

foo()
bar()
