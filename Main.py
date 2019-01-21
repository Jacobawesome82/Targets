import random
speed(0)
color_choice_two = ("red")
color_choice_one = ("black")
penup()
setposition(random.randint(-150, 150), random.randint(-150, 150))
pendown()
penup()
setposition(-754, -723)
player_one_name = input("Player 1, enter your name     ")
player_two_name = input("Player 2, enter your name     ")
if player_one_name == ("Jacob") or player_two_name == ("Jacob") or player_one_name == ("Cody") or player_two_name == ("Cody"):
    print("Hello Creators!")
else: 
    print("nice to meet you!")
dart_color_one = input("What color of darts do you want " + player_one_name +"?  ")
dart_color_two = input("what color of darts do you want " + player_two_name +"?  ")
radius = 100
if dart_color_one == ("black") or dart_color_two == ("black"):
    color_choice_one = ("white")
    if dart_color_one == ("white") or dart_color_two == ("white"):
        color_choice_one = ("purple")
if dart_color_one == ("red") or dart_color_two == ("red"):
    color_choice_two = ("blue")
    if dart_color_one == ("blue") or dart_color_two == ("blue"):
        color_choice_two = ("green")

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
    
print(player_one_name)
dart_x = int(input("try to hit the center! on X "))
dart_y= int(input("try to hit the center! on Y  "))
penup()
print(player_two_name)
dart_a = int(input("try to hit the center! on X "))
dart_z= int(input("try to hit the center! on Y  "))
penup()
color(dart_color_one)
setposition(dart_x, dart_y-3)
pendown()
begin_fill()
circle(6)
end_fill()
penup()
color(dart_color_two)
setposition(dart_a, dart_z-3)
pendown()
begin_fill()
circle(6)
end_fill()
penup()
setposition(990, 909)

def player_one_wins():
    print Player_one_name + "wins!"
def player_two_wins():
    print player_two_name + "wins!"
