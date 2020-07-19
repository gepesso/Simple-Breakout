# BreakOut_Pong game

import turtle
import random
import tkinter as tk
from tkinter import messagebox

wn = turtle.Screen()
wn.title("BreakOut Pong")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0, 0)

# Score initiate
score = 0

# draw paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=.5, stretch_len=5)
paddle.penup()
paddle.goto(0, -350)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=.5, stretch_wid=.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 1.2
ball.dy = -1.2

# Draw the breakout
breakout = turtle.Turtle()
breakout.speed(0)
breakout.shape("square")
colorrand = random.choice([0,1,2])
if colorrand == 0:
    breakout.color("blue")
    scoretype = 1
if colorrand == 1:
    breakout.color("green")
    scoretype = 2
if colorrand == 2:
    breakout.color("red")
    scoretype = 3

breakout.shapesize(stretch_len=5, stretch_wid=1)
breakout.penup()
xrand = random.randrange(-250, 250, 25)
yrand = random.randrange(-200, 350, 25)
breakout.goto(xrand, yrand)

# Pen for score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)

# Pen for coordinates
penc = turtle.Turtle()
penc.speed(0)
penc.color("white")
penc.penup()
penc.hideturtle()
penc.goto(-300, 350)


# pen.write("Score 0", align="center", font=("courier", 24))

# paddle moves
def paddle_left():
    x = paddle.xcor()
    if x > -240:
        x -= 20
        paddle.setx(x)
    else:
        x = -240


def paddle_right():
    x = paddle.xcor()
    if x < 240:
        x += 20
        paddle.setx(x)
    else:
        x = 240


def quitscreen():
    global exitVar
    exitVar = False


def resumescreen():
    global exitVar
    exitVar = True


def newBreakout():
    global scoretype
    colorrand = random.choice([0, 1, 2])
    if colorrand == 0:
        breakout.color("blue")
        scoretype = 1
    if colorrand == 1:
        breakout.color("green")
        scoretype = 2
    if colorrand == 2:
        breakout.color("red")
        scoretype = 3
    xrand = random.randrange(0, 250, 25) * random.choice([1, -1])
    yrand = random.randrange(0, 300, 25) * random.choice([1, -.5])
    breakout.setx(xrand)
    breakout.sety(yrand)


# Keybord input
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(quitscreen, "q")
wn.onkeypress(resumescreen, "w")

# main area of the game
exitVar = True
lives = 3

while exitVar:
    wn.update()

    # Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # print score
    pen.clear()
    pen.write("Score {} lives {}".format(score, lives), align="center", font=("courier", 20))
    # penc.clear()
    # penc.write("ball x {} y {}\n breakout x {} y {} x+50 {} x-50 {}".format(ball.xcor(), ball.ycor(), breakout.xcor(), breakout.ycor(), breakout.xcor()+50, breakout.xcor()-50),
    #           align="left")
    # Check border
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1

    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1

    if ball.ycor() < -390:
        ball.goto(0, 0)
        lives -= 1
        # if lives equal zero, then lost the game
        if lives <= 0:
            tk.messagebox.showinfo("You Lost!", "You Lost!")
            exit()

    # Ball bounces on paddle
    if ball.ycor() < -340 and (paddle.xcor() + 47 > ball.xcor() > paddle.xcor() - 47):
        ball.sety(-340)
        ball.dy *= -1

    # Ball bounces on breakout
    if (breakout.ycor() + 5 >= ball.ycor() >= breakout.ycor() - 5) and (breakout.xcor() + 55 >= ball.xcor() >= breakout.xcor() - 55):
        print("scoretype ", scoretype, " score ", score)
        ball.dy *= -1
        score += scoretype
        newBreakout()

        print("scoretype ", scoretype, " score ", score)

turtle.mainloop()
