# Rock-paper-scissors-lizard-Spock 
# Andreea Raducanu, 10.06.2015, Barcelona


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
def name_to_number(name):
    if name=="rock":
        name=0
    elif name=="Spock":
        name=1
    elif name=="paper":
        name=2
    elif name=="lizard":
        name=3
    elif name=="scissors": 
        name=4
    elif (name!="rock") and (name!="Spock") and (name!="paper") and (name!="lizard") and (name!="scissors"):
        name="Please choose between rock, Spock, paper, lizard, scissors!"
    return name
    # convert name to number using if/elif/else


def number_to_name(number):
    if number==0:
        number="rock"
    elif number==1:
        number="Spock"
    elif number==2:
        number="paper"
    elif number==3:
        number="lizard"
    elif number==4: 
        number="scissors"
    elif (number!=0) and (number!=1) and (number!=2) and (number!=3) and (number!=4):
        number="Please choose between 0, 1, 2, 3, 4!"
    return number
    # convert number to a name using if/elif/else
    

def rpsls(player_choice): 
    print("\n")    
    # print a blank line to separate consecutive games
    
    print "Player chooses " + player_choice
    # print out the message for the player's choice
    
    player_number=name_to_number(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    
    import random
    comp_number=random.randrange(0,5)
    # compute random guess for comp_number using random.randrange()

    comp_choice=number_to_name(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    
    print "Computer chooses " + comp_choice
    # print out the message for computer's choice

    diff=comp_number-player_number
    # compute difference of comp_number and player_number modulo five
    
    if diff%5==4 or diff%5==3:
        print"Player wins!"
    elif diff%5==2 or diff%5==1:
        print"Computer wins!"
    elif diff%5==0:
        print"Player and computer tie!" 
    # use if/elif/else to determine winner, print winner message

    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



