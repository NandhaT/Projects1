import random
import turtle

win=turtle.Screen()
win.title("Pong by Nandha")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# Score
scorea = 0
scoreb = 0

# life1a^
life1a = turtle.Turtle()
life1a.shape("triangle")
life1a.color("white")
life1a.penup()
life1a.goto(-380, -270)

# life2a^
life2a = turtle.Turtle()
life2a.shape("triangle")
life2a.color("white")
life2a.penup()
life2a.goto(-350, -270)

# life3a^
life3a = turtle.Turtle()
life3a.shape("triangle")
life3a.color("white")
life3a.penup()
life3a.goto(-320, -270)

# life1b^
life1b = turtle.Turtle()
life1b.shape("triangle")
life1b.color("white")
life1b.penup()
life1b.goto(310, -270)

# life2b^
life2b = turtle.Turtle()
life2b.shape("triangle")
life2b.color("white")
life2b.penup()
life2b.goto(340, -270)

# life3b^
life3b = turtle.Turtle()
life3b.shape("triangle")
life3b.color("white")
life3b.penup()
life3b.goto(370, -270)


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= (-1 or 1)

        scorea += 1
        if scorea == 1:
            life3b.color("Red")

        if scorea == 2:
            life2b.color("Red")

        if scorea == 3:
            life1b.color("Red")
            ball.dx *= 0
            ball.dy *= 0
            ball.hideturtle()
            pen.goto(0, 0)
            pen.write("Player 1 Wins!", align="center", font=("sans serif", 30, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= (-1 or 1)

        scoreb += 1
        if scoreb == 1:
            life1a.color("Red")

        if scoreb == 2:
            life2a.color("Red")

        if scoreb == 3:
            life3a.color("Red")
            ball.dx *= 0
            ball.dy *= 0
            ball.hideturtle()
            pen.goto(0, 0)
            pen.write("Player 2 Wins!", align="center", font=("sans serif", 30, "bold"))

    if paddle_a.ycor() < -370:
        paddle_a.sety(370)

    if paddle_a.ycor() > 370:
        paddle_a.sety(-370)

    if paddle_b.ycor() < -370:
        paddle_b.sety(370)

    if paddle_b.ycor() > 370:
        paddle_b.sety(-370)

    # Paddle and Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1

