"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game

jml 3/29/25 updated add the following:
--Change the input prompt to your initials and a colon. Ex. mss:
--Change the percentage that goes to the house to 12 percent instead of 10 
    percent.
--In the program introduction, include a notice that if the user gets a 2 
    or a 7 on a dice roll, they get a 10 mon bonus.
--If the dice roll is equal to a 2 or a 7, output a message to the user 
    what the total of roll was and that they got a 10 mon bonus. Then 
    add that bonus to the purse."""

import random, sys

prompt = 'jml:' #Input Prompt

#Function that calculates the rake. The rake percentage is configurable
def rake(pot, rake= 10):
    rake = pot // rake #Calculate the rake
    return(rake)

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}


print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number. If the player gets a 2 
or a 7 on a dice roll, there is a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input(prompt)
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input(prompt).upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)
    
    #award bonus mon if appropriate
    score = dice1 + dice2 #determine Score
    if score in [2,7]: #check if the score is a 2 or 7
        print(f"\nyour score was {score}! you won a 10 mon bonus!\n")
        purse +=10

    # Determine if the player won:
    rollIsEven = score % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'
    
    playerWon = bet == correctBet
    

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        print('The house collects a', rake(pot,False,rake=12), 'mon fee.')
        purse = purse - rake(pot,12)  # The house fee is 12%.
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
