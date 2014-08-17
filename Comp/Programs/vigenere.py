BASE = ord('a')

def intro():
    ''' This introduces the program to the users. '''
    print 'This program reads in two files and decrypts the'
    print 'ciphertext in the first file with the Vigenere'   
    print 'cipher and keywords found in the second file.'
    print

def letter(l1,l2):
    '''Takes a single letter'''
    x = ord(str(l1))-BASE
    x -= int(ord(l2)-BASE)
    if x < 0:
        x += 26
    return chr(x+BASE)

def decode(line,key):
    '''Decodes a line'''
    row = [0]*len(line)
    j = 0
    for i in range(0,len(line)):
        if j >= len(key):
            j = 0
        row[i] = letter(line[i],key[j])
        j += 1
    print ''.join(row)

def extract():
    '''Extracts out the line of both files'''
    txt = raw_input('Ciphertext file? ')
    key = raw_input('Keyword file? ')
    f = open(txt,'r')
    g = open(key,'r')
    cipherlist = []
    keylist = []
    for line in f:
        cipherlist.append(line.strip())
    for line in g:
        keylist.append(line.strip())
    for line in range(0,len(cipherlist)):
        decode(cipherlist[line],keylist[line])

intro()
extract()
