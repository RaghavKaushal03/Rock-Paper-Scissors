import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""

def choice_to_number(choice):
    if(choice=='rock'):
        return 0
    elif(choice=='paper'):
        return 1
    elif(choice=='scissors'):
        return 2

def number_to_choice(number):
    if(number==0):
        return 'rock'
    elif(number==1):
        return 'paper'
    elif(number==2):
        return 'scissors'

def random_computer_choice():
    options=['rock','paper','scissors']
    return random.choice(options)

def choice_result(computer_choice, human_choice):

    global COMPUTER_SCORE
    global HUMAN_SCORE

    if human_choice == 'rock' and computer_choice == 'paper':
        COMPUTER_SCORE = COMPUTER_SCORE + 1
        print("computer wins")
    elif human_choice == 'rock' and computer_choice == 'scissors':
        HUMAN_SCORE = HUMAN_SCORE +1
        print("human wins")
    elif human_choice == 'rock' and computer_choice == 'rock':
        print("Tie")
    elif human_choice == 'paper' and computer_choice == 'scissors':
        COMPUTER_SCORE = COMPUTER_SCORE + 1
        print("computer wins")
    elif human_choice == 'paper' and computer_choice == 'rock':
        HUMAN_SCORE = HUMAN_SCORE +1
        print("human wins")
    elif human_choice == 'paper' and computer_choice == 'paper':
        print("Tie")
    elif human_choice == 'scissors' and computer_choice == 'scissors':
        print("Tie")
    elif human_choice == 'scissors' and computer_choice == 'rock':
        COMPUTER_SCORE = COMPUTER_SCORE + 1
        print("computer wins")
    elif human_choice == 'scissors' and computer_choice == 'paper':
        HUMAN_SCORE = HUMAN_SCORE +1
        print("human wins")

# This code is for the GUI part of the game.
def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
    
# Handler for mouse click on paper button.
def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

# Handler to draw on canvas
def draw(canvas):
    
    try:
        # Draw choices
        canvas.draw_text("You: " + human_choice, [10,40], 48, "Green")
        canvas.draw_text("Comp: " + computer_choice, [10,80], 48, "Red")
        
        # Draw scores
        canvas.draw_text("Human Score: " + str(HUMAN_SCORE), [10,150], 30, "Green")
        canvas.draw_text("Comp Score: " + str(COMPUTER_SCORE), [10,190], 30, "Red")
        
    except TypeError:
        pass
    

# Create a frame and assign callbacks to event handlers
def play_rps():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()
 
play_rps()
