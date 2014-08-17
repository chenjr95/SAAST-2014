def introduction():
    ''' This introduces the program to the user. '''
    print "This program decrypts a message encrypted"
    print "with a ceaser cipher by brute-force.  The"
    print "text given must be lowercase with no spaces."  
    print
    
def cipher(count = 0):
    ''' This checks the input to make sure it is valid and
        calls the decryption function to decrypt the input. '''
    script = ""
    script = raw_input("Ciphertext? ").strip()
    while script.islower() == False or script.isalpha() == False:
        script = raw_input("Invalid input. Ciphertext should only contain lower-cased letters. ")
    length = len(script)
    decryption(count, length, script)

def decryption(count, length, script):
    ''' This calls another function and adds the decrypted letters
        together and prints the decrypted word. '''
    print "n = " + str(count) + ": ",
    final=''
    for i in range(0, length):
        final = final + single_letter(i,script,count)
    print final,
    count = count + 1
    again(count, length, script)

def single_letter(i,script,count):
    ''' This decrypts a single letter and returns the result. '''
    BASE = ord("a")
    result = ord(script[i]) - BASE
    letter = (result - count)%26   
    final = chr(letter + BASE)
    return final

def again(count, length, script):
    ''' This asks the user if the output is correct. If it is not, this
        program cycles through another decryption of the input until the
        user says the decryption is correct. If the user does not, after
        26 cycles, the program terminates and a decryption is not found. '''
    while count <= 25:
        print ""
        again = raw_input("Is this the correct decryption? ").lower().strip()
        while again != "yes" and again != "y" and again != "no" and again != "n":
            again = raw_input("Is this the correct decryption [y/n] ").lower().strip()
        if again == "n" or again == "no":
            decryption(count, length, script)
        if again == "y" or again == "yes":
            print "Message decrypted!"
        return again
    if count == 26:
        print ""
        again = raw_input("Is this the correct decryption? ").lower().strip()
        while again != "yes" and again != "y" and again != "no" and again != "n":
            again = raw_input("Is this the correct decryption [y/n] ").lower().strip()
        if again == "n" or again == "no":
            print "Message not decrypted!"
        if again == "y" or again == "yes":
            print "Message decrypted!"

introduction()
cipher()
