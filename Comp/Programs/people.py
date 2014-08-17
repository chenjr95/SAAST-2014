NUM_PEOPLE = 4

#Function parameters/arguments

def first_line(index):
    print ' ' * (2 + 5 * ((NUM_PEOPLE -1) - index)) + \
            'O  ' +     \
            '*'*6  +     \
            ' '*(5*index) +    \
            '*'

def second_line(i):
    print ' ' * (1+5 * ((NUM_PEOPLE -1)-i)) + \
              '/|\ *' + \
              ' ' * 5 * (i +1) +\
              '*'

def third_line(barf):
    print ' ' * (1+5*((NUM_PEOPLE -1)-barf)) +\
              '/ \ *' +\
              ' ' * 5 * (barf + 1) +\
              '*'
    
def people():
    for i in range(0,NUM_PEOPLE):
        first_line(i)
        #Print Second Line
        second_line(i)
        third_line(i)
       
def border():
    print'*'*(12+5*(NUM_PEOPLE - 1))

people()
border()
