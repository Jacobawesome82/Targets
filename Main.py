import random
speed(0)
penup()
target_x = random.randint(-150, 150)
target_y = random.randint(-150, 150)
setposition(target_x, target_y)
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

score1 = (50 - abs(abs(target_x) - abs(p1_x))) + (50 - abs((abs(target_y) + 25) - abs(p1_y)))
if score1 < 0:
    score1 = 0

score2 = (50 - abs(abs(target_x) - abs(p2_x))) + (50 - abs((abs(target_y) + 25) - abs(p2_y)))
if score2 < 0:
    score2 = 0

print("Player one score: " + str(score1))
print("Player two score: " + str(score2))

setposition(990, 909)
