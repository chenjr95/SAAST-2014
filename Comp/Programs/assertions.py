def easy(x,y):
    while x>0:
        #POINT A
        if x>0:
            x=x-y
        if x<y:
            x=x-y
        #POINT B
    while y>0:
        #POINT C
        if x<0:
            y=y+x
        else:
            y=y-1
    #POINT D
    return x+y



def hard(x, y, z):
    if x>= 0:
        return -1
    else:
        #POINT A
        while x<0:
            #POINT B 
            if y>0:
                if x>0:
                    return True
                if z>0:
                    x=x+y
                elif z+y<0:
                    x=x+y
            elif y<0:
                if x>0 and y>0:
                    return True
                if z>0:
                    x=x-y
                elif z<=0:
                    x=x-y
                #POINT C
            else:
                x=x+1
        if x<0:
            return True
        while 1<x<3:
            if y > 0:
                x=x+y
            if y < 0:
                x=x-y
        #POINT D
        return x+y

v=easy(4,4)
print v
w=hard(1,2,4)
print w
