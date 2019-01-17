import random
speed(0)
penup()
setposition(random.randint(-150, 150), random.randint(-150, 150))
pendown()

def next_circle():
    left(270)
    penup()
    forward(25)
    pendown()
    left(90)
radius=25

def player_guess(player):
    print(player)
    xvar = int(input("try to hit the center! on X "))
    yvar= int(input("try to hit the center! on Y  "))
    return xvar, yvar

def place_dart(x, y, p_color):
    color(p_color)
    setposition(x, y - 3)
    pendown()
    begin_fill()
    circle(6)
    end_fill()
    penup()

for i in range (4):
    circle(radius)
    radius += 25
    next_circle()

penup()
setposition(-754, -723)
dart_color_one = input("What color of darts do you want player 1?  ")
dart_color_two = input("what color of darts do you want player 2?  ")

p1_x, p1_y = player_guess("player 1")

p2_x, p2_y = player_guess("player 2")

place_dart(p1_x, p1_y, dart_color_one)

place_dart(p2_x, p2_y, dart_color_two)

penup()
setposition(-210, -210)
