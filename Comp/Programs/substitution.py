def intro():
    """introduction to the program"""
    print "This program reads in ciphertext in one file"
    print "and a substitution table from another file and"
    print "writes the decrypted plaintext to a third file"
    print "using the table."
    print

def cipher():
    """this is the cipher for all the lines of the file, it makes a table/dictionary
    and uses it to replace the text"""
    x = raw_input("Ciphertext file? ")
    text = open(x, "r")
    y = raw_input("Table file? ")
    table = open(y, "r")
    z = raw_input("Output file? ")
    output = open(z, "w")
    x1 = []
    x2 = []
    for line in table:
        x1.append(line.strip())
    for i in range(97, 123):
        x2.append(chr(i))
    tbl = {x2[k]:x1[k] for k in range(0,26)}
    for line in text:
        line = line.strip()
        line1(line, output, tbl)
        output.write("\n")

def line1(line, output, tbl):
    """this decodes just one line"""
    for i in range(0, len(line)):
        output.write(tbl[line[i]])
    return line
    
    
    
intro()
cipher()
