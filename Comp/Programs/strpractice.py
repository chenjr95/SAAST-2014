def print_lineified(word):
    word_length=len(word)
    for i in range(0,word_length):
        print word[i]

def intersperse(string, sep=' '):
    string_length=len(string)
    x=string[0]
    for i in range(1,string_length):
        x=x+sep+string[i]
    return (x)

def swap(string2, index):
    string2_length=len(string2)
    y=string2[(index):string2_length]+string2[0:(index)]
    return (y)


print_lineified('vertical')
print intersperse('this is an example string', sep = '-')
print intersperse('whydidyouforgetthespaces?')
print swap('swapme', 2)
print swap('abcdefghijklmnopqrstuvwxyz',13)
print swap('hello world',1)
