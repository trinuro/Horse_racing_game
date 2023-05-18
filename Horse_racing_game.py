from turtle import *
import time
import random

WIDTH, HEIGHT = 500, 500
#define two global constants 
COLOURS = ["red", "orange", "maroon", "magenta", "navy", "cyan", "blue", "brown", "black", "white"]

def get_racer_number() -> int:
    racers = 0
    while True:
        racers = input("How many racers are there? (2-10): ")
        if racers.isdigit():
            racers = int(racers)
            if racers in range(2,11):
                return racers
            else:
                print("Please enter number between 2 to 10")
                continue
        else:
            print("Please enter a digit")
            continue
# Used to receive the number of racers

def init_background() -> None:
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    # Used to initialise the screen and set the width and height of screen
    screen.title("Kuching Horse Racing")
    # Change name of the window
    screen.bgcolor("green")
#Initialise environment variable for turtle

def init_horse(colour_list: list) ->list:
    horses = list()
    for i, colour in enumerate(colour_list):
        horse = Turtle()
        horse.color(colour)
        horse.left(90)
        horse.penup()
        horse.setpos(450/(len(colour_list)+1)*(i+1)-225, -230)
        horse.pendown()
        horse.speed(random.randint(5,7))
        horses.append(horse)

    return horses
#Initialise horses and move them to correct position

def race(colour_list: list) -> tuple:
    horses = init_horse(colour_list)
    while True:
        for horse in horses:
            distance = random.randrange(1,15)
            horse.forward(distance)

            x,y = horse.pos()
            if y >= HEIGHT//2 - 10:
                return horse.color()
#Race the horses to finish line

def play() -> None:
    number_of_horses = get_racer_number()
    init_background()

    random.shuffle(COLOURS)
    #shuffle the constant list COLOURS
    colours = COLOURS[:number_of_horses]

    winner_tuple = race(colours)
    time.sleep(1)
    print("The winner is {} horse".format(winner_tuple[0]))
# Play the game (Actual code here)

while True:
    play_or_not = input("\n!!Welcome to the Horse Race!! \n Would you like to play? (Yes/No)  ").lower()
    if play_or_not == "yes":
        play()
        clearscreen()
    elif play_or_not == "no":
        exit()
    else: 
        print("Enter Yes or No")




