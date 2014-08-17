class Point(object):
    '''
    A basic Point object (x,y).

    Attributes/fields:
    x - x-coordinate
    y - y-coordinate
    '''

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def translate(self, dx, dy):
        ''' Shirfts this point by (dx,dy)'''
        self.x += dx
        self.y += dy

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

##    def __plus__(self, other):
##        return Point(self.x + other.x, self.y + other.y)
    
p1= Point(0,0)
p2 = Point(3,5)
p3 = p1 + p2
p1.translate

print p1
print p2
print p3
