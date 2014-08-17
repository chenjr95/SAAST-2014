import random

TOTAL_YEARS=10

def results(player, computer):
    ''' This function determines the appropriate dialogue resulting from
        the strategies of each player '''
    if player == 'peace' and computer == 'peace':
        print '>>> Peace for everyone!'
    if player == 'war' and computer == 'war':
        print '>>> Everyone to arms!'
    if player == 'peace' and computer == 'war':
        print '>>> They crushed us!'
    if player == 'war' and computer == 'peace':
        print '>>> We crushed them!'

def pscoreresults(player, computer):
    ''' This function returns the appropriate points for the player '''
    if player == 'peace' and computer == 'peace':
        return 3
    if player == 'war' and computer == 'war':
        return 1
    if player == 'peace' and computer == 'war':
        return 0
    if player == 'war' and computer == 'peace':
        return 5

def cscoreresults(player, computer):
    ''' This function returns the appropriate points for the computer '''
    if player == 'peace' and computer == 'peace':
        return 3
    if player == 'war' and computer == 'war':
        return 1
    if player == 'peace' and computer == 'war':
        return 5
    if player == 'war' and computer == 'peace':
        return 0

def finalresults(total_played, total_won):
    ''' This function displays the final results after all games are played '''
    print 'Total games played: ' + str(total_played)
    print 'Total games won: ' + str(total_won)
    print 'Percentage won: %' + str(100.0*total_won/total_played)[0:5]

def play_again(total_played, total_won):
    ''' This function determines whether the player wants to play again and
        takes the appropriate action '''
    print
    answer = raw_input('Play again? ').lower().strip()
    while answer != 'y' and answer != 'n' and answer != 'yes' and answer != 'no':
        answer = raw_input('Invalid response.  Please enter "y" or "n". ').lower().strip()        
    if answer=='y' or answer == 'yes':
        all_games(total_played, total_won)
    else:
        finalresults(total_played, total_won)
        
def game():
    ''' This function plays through a single game '''
    year = 0
    pscore = 0
    cscore = 0
    strategy=''
    for i in range (1,TOTAL_YEARS+1):
        print '====='
        print 'Year ' + str(i)
        print 'Our score: ' + str(pscore)
        print 'Their score: ' + str(cscore)
        print
        compstrategy= computer_ai(strategy)
        strategy=raw_input('What is your strategy this year? ').lower().strip()
        while strategy != 'peace' and strategy != 'war':
            strategy=raw_input('Invalid strategy.  Enter "peace" or "war": ').lower().strip()
        print 'You chose ' + strategy
        print 'They chose ' + compstrategy
        results(strategy, compstrategy)
        pscore=pscore+pscoreresults(strategy,compstrategy)
        cscore=cscore+cscoreresults(strategy,compstrategy)
    print '====='
    print 'Final'
    print 'Our score: ' + str(pscore)
    print 'Their score: ' + str(cscore)
    print
    if pscore>cscore:
        print '>>>>> We win! <<<<<'
        return 1
    elif pscore<cscore:
        print '>>>>> They win! <<<<<'
        return 0
    else:
        print ">>>>> It's a tie <<<<<"
        return 0
    
def all_games(total_won=0,total_played=0):
    ''' This function plays through all the games '''
    total_won=total_won+game()
    total_played=total_played+1
    play_again(total_played, total_won)
     
def computer_ai(strategy):
    ''' This function gives the computer player a.i. to use against the player '''
    if strategy=='':
        return 'peace'
    if strategy=='peace':
        return 'peace'
    if strategy=='war':
        return 'war'
    
all_games()
