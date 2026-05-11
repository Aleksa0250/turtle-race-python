import turtle
import time
import random

WIDTH, HEIGHT = 500,500
COLORS = ["red", "green", "blue", "yellow", "cyan", "magenta", "brown", "pink","purple", "orange", "gold", "teal"]

def get_number_of_racers():

    while True:
        try:
            racers = int(input("Enter number of racers (2-10): "))
            if racers < 2 or racers > 10:
                print("Please enter a number between 2 and 10.")
            else:
                break

        except ValueError:
            print("Please enter a number.")

    return racers
def race(colors):
    turtles = create_turtles(colors)


    while True:
        for racer in turtles:
            distance= random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx= WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 +20)
        racer.pendown()
        turtles.append(racer)
    return turtles
def init_turtles():
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title("Race")


racers=get_number_of_racers()
init_turtles()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"The winner is {winner} !")
turtle.done()
