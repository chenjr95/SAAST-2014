def print_numbers(y):
    for i in range(1,y+1):
        print '[' + str(i) + ']',

def print_powers(w, x):
    for i in range(0, x+1):
        print w**i,

def print_square(x,y):
            diff = y-x
            for i in range(0,y-2):
                      for j in range(i,diff+i+1):
                          print j%(diff+1)+x,
                      print

print_numbers(15)
print
print_numbers(5)
print
print_powers(4,3)
print
print_powers(5,6)
print
print_powers(-2,8)
print
print_square(3,7)


