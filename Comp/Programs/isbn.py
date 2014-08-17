def calc_check_digit(isbn):
    x=0
    i=1
    while i<10:
        x=x+i*int(isbn[i-1])
        i=i+1
    x=x%11
    return x

def prompt():
    print 'This program checks to see if a given ISBN is valid.'
    print 'It can process ISBN-10 codes.'

def check_isbn(isbn):
    x=calc_check_digit(isbn)
    if isbn[9]=='X':
        if x==10:
            print isbn + ' is a valid ISBN-10 code.'
            return True
        else:
            print isbn + ' is not a valid ISBN-10 code.'
            print 'Expected ' + str(x) + ', but found X.'
            return False
    else:
        if x==int(isbn[9]):
            print isbn + ' is a valid ISBN-10 code.'
            return True
        else:
            print isbn + ' is not a valid ISBN-10 code.'
            print 'Expected ' + str(x) + ', but found ' + isbn[9] + '.'
            return False
        
prompt()
isbn = raw_input('Enter the ISBN-10 code to check: ')
check_isbn(isbn)
