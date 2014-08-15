from math import sqrt

def distance(x1,x2,y1,y2,z1=0,z2=0):
    return (((x1-x2)**2)+((y1-y2)**2)+((z1-z2))**2)**(0.5)

def string_seq(lo,hi):
    x=str(lo)
    for i in range (lo+1, hi+1):
        x=x+'-'+str(i)
    return(x)

print distance(3,8,-2,4,1.8,6)
print distance(1,4,0,4)
print string_seq(0,5)
print(string_seq(2,9))
