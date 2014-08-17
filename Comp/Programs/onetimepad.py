def intro():
    ''' This is the introduction to the program. '''
    print 'This program decrypts a line of text using a'
    print 'one-time pad.  The ciphertext is encrypted with'
    print 'a key of the same length as the ciphertext.'
    print

def text_and_key():
    ''' This computes whether the text and the key are valid.
        It also ands the decrypted characters together and prints
        the results. '''
    new_text=''
    text= raw_input('Ciphertext? ')
    if text.isalpha() != True or text.islower() != True:
        print 'Error: ciphertext must contain only lower-case letters.'
        return
    key= raw_input('Key? ')
    if key.isalpha() != True or key.islower() != True:
        print 'Error: key must contain only lower-case letters.'
        return
    if len(text) != len(key):
        print 'Error: ciphertext and key are not the same length.'
        return
    for i in range(0, len(text)):
        new_text=new_text+single_char(text[i],key[i])
    print new_text

def single_char(t,k):
    ''' This decrypts a single character and returns the result. '''
    new=((ord(t)-(ord(k))))%26
    new=chr(new+ord('a'))
    return new

intro()
text_and_key()
