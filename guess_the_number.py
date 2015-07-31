# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# Andreea Raducanu, 10.06.2015, Barcelona

# helper function to start and restart the game
import random
import simplegui
import math

num_range = 100
remaining_guesses = 7

def new_game():
    # initialize global variables used in your code here
    global secret_number, remaining_guesses
    secret_number = random.randrange(0, num_range)
    remaining_guesses = int(math.ceil(math.log(num_range,2)))
    print 'Enter your guess or choose a range!'
    return secret_number
# define event handlers for control panel

def range100():
    # button that changes the range to [0,100) and starts a new game 
    print 'Range is [0, 100)'
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print 'Range is [0, 1000)'
    global num_range
    num_range = 1000
    new_game()

def input_guess(guess):
    global remaining_guesses
    remaining_guesses -= 1
    print 'Guess was',int(guess)
    if remaining_guesses == 0:
        print 'You are out of guesses. Play a new game! \n' 
        new_game()
    elif secret_number == int(guess):
        print 'Correct! You win! \n'
        new_game()
    elif secret_number > int(guess):
        print 'Number is higher! \nYou have',remaining_guesses,'remaining guesses.'
    elif secret_number < int(guess): 
        print 'Number is lower! \nYou have',remaining_guesses,'remaining guesses.'
        
# create frame
frame = simplegui.create_frame('Guess the number', 150, 150)
frame.add_input('Enter your guess:', input_guess, 114)
frame.add_button('Range 0-100', range100, 120)
frame.add_button('Range 0-1000', range1000, 120)


# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


