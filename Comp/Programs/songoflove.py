'''This program reproduces the song, "Song of Love" without redundancy.'''

def intro():
    print "I like you, Fred, I like you!"
    print "You're just saying those words to be kind."
    print "No, I mean it.  I like... I mean I love you, Fred!"
    print "He is out of his medieval mind!"
    print "I'm perfectly sane and sound!  I never felt better in my life!"
    print "Everybody... everybody, everybody!  Come on!  And meet my incipient wife!"

def conclusion():
    print "\nI'm in love with a girl."
    print "He's in love with a girl named \"F-R-E-D\" Fred!"

def firstline():
    print "\nI'm in love with a girl named Fred."

def verse1a():
    firstline()
    print "My reasons must be clear."
    print "When she shows you all how strong she is you'll stand right up and cheer!"
    fred()
    
def fred():
    print 'With a "F" and a "R" and an "E" and a "D"'
    print 'And a "F-R-E-D" Fred!  Yeah!'

def verse2a():
    firstline()
    print "She drinks just like a lord!"
    print "So sing a merry drinking song and let the wine be poured!"
    goblet()
    
def goblet():
    print "Fill the bowl to overflowing.  Raise the goblet high!"
    fred()

def verse3a():
    firstline()
    print "She sings just like a bird!"
    print "You'll be left completely speechless when her gentle voice is heard!"
    singing()
    
def singing():
    print "La la la la, la la la la, la la la la la!"
    goblet()

def verse4a():
    firstline()
    print "She wrestles like a Greek!"
    print "You will clap your hands in wonder at her fabulous technique!"
    clap()

def clap():
    print "Clap clap, clap clap, clap clap clap clap, clap, clap clap!"
    singing()

def verse5a():
    firstline()
    print "She dances with such grace!"
    print "You are bound to sing her praises 'til you're purple in the face!"
    bravo()

def bravo():
    print "Bravo!  Bravo!  Bravissimo bravo!  Bravissimo!"
    clap()
    
def verse6a():
    firstline()
    print "She's musical to boot!"
    print "She will set your feet a-tapping when she plays upon her lute!"
    strum()

def strum():
    print "Strum strum, strum strum, strum strum strum strum strum, strum."
    bravo()

def verse7a():
    firstline()
    print "A clever, clownish wit!"
    print "When she does her funny pantomime your sides are sure to split!"
    laugh()
    
def laugh():
    print "Ha ha ha ha, ho ho ho ho, ha ha ha ha ho!"
    strum()

def song():
    intro()
    verse1a()
    verse2a()
    verse3a()
    verse4a()
    verse5a()
    verse6a()
    verse7a()
    conclusion()

song()
