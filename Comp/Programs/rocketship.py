SUB_HEIGHT = 3

def border():
    print "+"   +\
          "=*"*(SUB_HEIGHT*2)  +\
          "+"

def cone():
    for i in range (0,((SUB_HEIGHT*2)-1)):
        print ' ' * (((SUB_HEIGHT*2)-1)-i) +\
              '/' * (i+1) +\
              '**'        +\
              '\\' * (i+1)

def body1():
    for i in range (0,SUB_HEIGHT):
        print '|'             +\
              '.' * ((SUB_HEIGHT-1)-i)     +\
              '/\\' * (i+1)   +\
              '.' * 2 * ((SUB_HEIGHT-1)-i) +\
              '/\\' * (i+1)   +\
              '.' * ((SUB_HEIGHT-1)-i)     +\
              '|'

def body2():
    for i in range ((SUB_HEIGHT-1),-1,-1):
         print '|'             +\
              '.' * ((SUB_HEIGHT-1)-i)     +\
              '\\/' * (i+1)   +\
              '.' * 2 * ((SUB_HEIGHT-1)-i) +\
              '\\/' * (i+1)   +\
              '.' * ((SUB_HEIGHT-1)-i)     +\
              '|'

cone()
border()
body1()
body2()
border()
body2()
body1()
border()
cone()
