def insert():
    w='My name is Chris'
    v='I wrote this'
    x=' '
    y=' '
    remove()
    redefine()
    print x+y
    
def remove():
    x=(1+5%2)/0.5
    y=1

def redefine():
    remove()
    str(x+y)
    

x='Hey '
y='there'
remove()
z=x+y
insert()
x=y+z
y=x+z
print z
insert()
