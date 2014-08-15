def lines():
    f = open('pg1661.txt', 'r')
    count = 0
    for line in f:
        count = count+1
    print 'This book is {} lines.'.format(count)

def words():
    f = open('pg1661.txt', 'r')
    word = 0
    for line in f:
        token=line.split()
        for tok in token:
            word=word+1
    print 'This book has {} words.'.format(word)
           
def characters():
    f = open('pg1661.txt', 'r')
    counts = 0
    for line in f:
        token=line.split()
        for tok in token:
            for ch in tok:
                ch=ch.lower()
                if ch.isalpha():
                    counts = counts + 1
    print 'This book has {} characters.'.format(counts)
    
def word_size():
    f = open('pg1661.txt', 'r')
    count = 0
    counts = 0
    for line in f:
        token=line.split()
        for tok in token:
            count = count + 1
            for ch in tok:
                ch=ch.lower()
                if ch.isalpha():
                    counts=counts+1
    wordsize=1.0*counts/count
    print 'The average word size in this book is {:.3} characters.'.format(wordsize)

lines()

words()

characters()

word_size()
