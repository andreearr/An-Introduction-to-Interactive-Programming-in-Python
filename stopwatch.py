# Andreea Raducanu, 16.06.2015, Barcelona

# define global variables
import simplegui

counter = 0
counter1 = 0
counter2 = 0
whole = 0
stopped = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global msec
    global sec
    global mins 
    global whole
    mins = 0 
    msec = (t % 10)
    sec = (t - msec ) // 10 
    sec1 = sec % 60
    mins = sec // 60 
    if msec > 9 :
        msec = 0 
        sec1 = sec1 + 1 
    if( sec1 > 59): 
        mins = mins + 1
        sec1 = sec1 - 60 
    sec_s = str(sec1) 
    if len(str(sec1)) == 1:
        sec_s = '0' + str(sec1)
    if t != 0 and msec == 0:
        whole = 1
    else:
        whole = 0
    return str(mins) + ':' + sec_s + '.' + str(msec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler1():
    global stopped
    stopped = 1
    timer.start()
        
def button_handler2():
    global counter2, counter1, counter, whole, stopped
    timer.stop()
    if whole == 1:
        counter1 += 1
        counter2 += 1
    elif stopped == 1:
        counter2 += 1
    stopped = 0

def button_handler3():
    global counter, counter1, counter2, stopped
    timer.stop()
    counter = 0
    counter1 = 0
    counter2 = 0 
    stopped = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1
        
# define draw handler
def draw_handler(canvas):
    global counter
    canvas.draw_text(str(format(counter)), (120, 150), 40, 'White')
    canvas.draw_text("Success rate: " + str(counter1) + "/" + str (counter2), (20, 20), 25, 'Red')
 
# create frame
# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame = simplegui.create_frame('Stopwatch', 300, 300)
frame.set_draw_handler(draw_handler)
button1 = frame.add_button('Start', button_handler1)
button2 = frame.add_button('Stop', button_handler2)
button3 = frame.add_button('Reset', button_handler3)

# start frame
frame.start()
