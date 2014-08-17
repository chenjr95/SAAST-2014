def people():
    for i in range(0,5):
        #Print a person
        for j in range(0,1):
            print ' '*(19-(i*5)+1),
        print' O  ******' + ' '*(i*5) + '*'
        for j in range(0,1):
            print ' '*(19-(i*5)+1),
        print'/|\ *' + ' '*5*(i+1) + '*'
        for j in range(0,1):
            print ' '*(19-(i*5) +1),
        print'/ \ *' + ' '*5*(i+1) + '*'
        


def border():
    print '*'*32

people()
border()
