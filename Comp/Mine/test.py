abc

defg

hijk

count = 0
def change (amt):
    if amt < 0:
        return 0
    elif amt == 0:
        return 1
    else:
        return change(amt-1) + change(amt-5) + change(amt-10) + change(amt-25) + change(amt-50)

def sum (i):
    if i == 0:
        return 0
    else:
        return i + sum(i-1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,p):
        return Point(self.x+p.x, self.y+p.y)

    def translate(self, p):
        self.x += p.x
        self.y += p.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return __str__

def main():
    p1 = Point(1,1)
    p2 = Point(2,2)
    p1.translate(p2)
    print p1 + p2

print "\""