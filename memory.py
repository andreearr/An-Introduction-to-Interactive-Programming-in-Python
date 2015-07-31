# implementation of card game - Memory
# Andreea Raducanu, 10.06.2015, Barcelona

import simplegui
import random


# helper function to initialize globals
def new_game():
    global list_final, exposed, state, choice, turns;
    list1 = range(0,8)
    list2 = range(0,8)
    list_final = list1 + list2
    random.shuffle(list_final)  
    exposed = [False]*16
    state = 0
    choice = [-1, -1]
    turns = 0
    label.set_text("Turns = " + str(turns))

# define event handlers
def mouseclick(pos):
    global state, choice, turns
    i = pos[0] // 50 
    if (state == 0): # Start of the game
        if (exposed[i] == False):
            if list_final[choice[0]] != list_final[choice[1]]:
                exposed[choice[0]] = False
                exposed[choice[1]] = False 
            exposed[i] = True
            choice[0] = i
            state = 1 
            turns = turns + 1
            label.set_text("Turns = " + str(turns))
    elif state == 1: # One card is exposed
        if exposed[i] == False:
            exposed[i] = True
            choice[1] = i
            state = 0
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list_final, exposed
    for i in range(len(exposed)):
        if exposed[i] == False:
           canvas.draw_polygon([(50 * i, 0), (50 * (i + 1), 0), (50 * (i + 1), 100),(50 * i, 100)], 3, "White", "Black");
        else:
           canvas.draw_text(str(list_final[i]), (50 * i, 90), 90, "Gray")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

