import turtle
import random
import time

WIDTH, HEIGHT = 700, 600   # constant values here
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_no_of_racers():
    racers = 0
    while True:
        racers = input("Enter number of racers (2 - 10): ")
        if not racers.isdigit():
            print("You did not enter number, Try again!")
            continue

        racers = int(racers)
        if 2 <= racers <= 10:
            return racers
        else:
            print("Your number is not in range (2 -10), Try again!")


def race(colors):
    turtles = create_turtles(colors)
    while True:
        for i, racer in enumerate(turtles):
            distance = random.randint(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 20:
                return colors[i]

def create_turtles(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingX, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing!")


racers = get_no_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is the turtle with color:{winner}")
time.sleep(5)