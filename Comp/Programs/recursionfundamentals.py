def print_halves(n):
    if n<=1:
        print n,
    else:
        print_halves(n/2)
        print ', ' + str(n),

def even_digits(n):
    if n==0:
        return 0
    else:
        x = n%10
        y = n/10
        z = even_digits(y)
        if x%2==0:
            return z+1
        else:   
            return z

def print_sequence(n):
    print 'n = ' + str(n) + ':',
    if n%2==0:
        for i in range(n/2, 0,-1):
            print i,
        for i in range (1, n/2+1):
            print i,
    else:
        for i in range(n/2+1,1,-1):
            print i,
        for i in range (1, n/2+2):
            print i,

def print_sequence(n):
    if n==1:
        print '1',
    elif n==2:
        print '1 1',
    else:
        print (n+1)/2,
        print_sequence(n-2)
        print (n+1)/2,

def test():
    print_halves(742)
    print
    print_halves(1)
    print
    print_halves(61)
    print
    print even_digits(3170)
    print even_digits(291875614)
    print_sequence(8)
    print

test()
