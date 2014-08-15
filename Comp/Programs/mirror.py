def border():
    print '#================#'

def mirror():
    for i in range (0,4) + range (3,-1,-1):
        print '|'          +\
              ' ' *(6-2*i) +\
              '<>'         +\
              '..'*(2*i)   +\
              '<>'         +\
              ' ' *(6-2*i) +\
              '|'

border()
mirror()
border()
