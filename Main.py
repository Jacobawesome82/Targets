#Setup
import random
speed(0)
penup()
target_x = random.randint(-150, 150)
target_y = random.randint(-150, 150)
color_choice_two = ("red")
color_choice_one = ("black")
radius = 100
setposition(target_x, target_y)
#Get player names
player_one_name = input("Player 1, enter your name     ")
player_two_name = input("Player 2, enter your name     ")
#Easter egg
if player_one_name == ("Jacob") or player_two_name == ("Jacob") or player_one_name == ("Cody") or player_two_name == ("Cody"):
    print("Hello Creators!")
else: 
    print("nice to meet you!")
#Get player colors
dart_color_one = input("What color of darts do you want " + player_one_name +"?  ")
dart_color_two = input("what color of darts do you want " + player_two_name +"?  ")
#Change dartboard so you can see the darts
if dart_color_one == ("black") or dart_color_two == ("black"):
    color_choice_one = ("white")
    if dart_color_one == ("white") or dart_color_two == ("white"):
        color_choice_one = ("orange")
if dart_color_one == ("red") or dart_color_two == ("red"):
    color_choice_two = ("blue")
    if dart_color_one == ("blue") or dart_color_two == ("blue"):
        color_choice_two = ("yellow")
pendown()

def next_a_circle(radius):
    left(90)
    penup()
    forward(25)
    pendown()
    left(270)

def make_circle(radius):
    color(color_choice_one)
    begin_fill()
    circle(radius)
    end_fill()

def make_circle_one(radius):
    color(color_choice_two)
    begin_fill()
    circle(radius)
    end_fill()
penup()
setposition(0, -150)
pendown()
for i in range(2):
    make_circle(radius)
    radius -= 25
    next_a_circle(radius)
    make_circle_one(radius)
    radius -=25
    next_a_circle(radius)

def player_guess(player):
    print(player)
    xvar = int(input("try to hit the center! on X "))
    yvar = int(input("try to hit the center! on Y "))
    return xvar, yvar

def place_dart(x, y, p_color):
    color(p_color)
    setposition(x, y - 3)
    pendown()
    begin_fill()
    circle(6)
    end_fill()
    penup()

penup()
setposition(-220, -220)

#get p1 & p2 coordinates
p1_x, p1_y = player_guess("player 1")
p2_x, p2_y = player_guess("player 2")

#Place p1 &p2 darts
place_dart(p1_x, p1_y, dart_color_one)
place_dart(p2_x, p2_y, dart_color_two)
#Calculate the score
score1 = (100 - abs(abs(target_x) - abs(p1_x))) + (100 - abs((abs(target_y) + 25) - abs(p1_y)))
if score1 < 0:
    score1 = 0

score2 = (100 - abs(abs(target_x) - abs(p2_x))) + (100 - abs((abs(target_y) + 25) - abs(p2_y)))
if score2 < 0:
    score2 = 0
#print scores
print("Player one score: " + str(score1))
print("Player two score: " + str(score2))

setposition(-220, -220)
def player_one_wins():
    print player_one_name + " wins!"
    setposition(-250, -250)
    dart_color_one
    begin_fill()
    circle(9999)
    end_fill()
    
def player_two_wins():
    print player_two_name + " wins!"    
    setposition(-250, -250)
    dart_color_two
    begin_fill()
    circle(9999)
    end_fill()
    
if score1 > score2:
    player_one_wins()
if score1 < score2:
    player_two_wins()
if score1 == score2:
    print "It's a tie!"
    
