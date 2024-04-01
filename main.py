from turtle import Turtle , Screen
import random

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'black']


screen = Screen()
def move_forward():
    timmy.forward(15)
def move_backward():
    timmy.backward(15)
def counter_clockwise():
    timmy.left(5)
def clockwise():
    timmy.right(5)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a colour:")

y = -150
for i in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(-300, y)
    y += 50

game_run = True
while game_run:
    for i in range(6):
        t = screen.turtles()
        t[i].forward(random.randint(0,10))
        if t[i].pos()[0] > 300:
            if user_bet == t[i].color()[0]:
                print(f"You win. {t[i].color()[0]} wins the race.")
                # screen.bye()
                game_run = False


            else:
                print(f"You loose. {t[i].color()[0]} wins the race.")
                game_run = False
                # screen.bye()





screen.exitonclick()
