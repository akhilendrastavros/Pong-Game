import turtle as t
playerAscore = 0
playerBscore = 0

window=t.Screen()
window.title("PONG")
window.bgcolor("cyan")
window.setup(width=800,height=600)
window.tracer(0)

leftpaddle= t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=8,stretch_len=0.5)
leftpaddle.penup()
leftpaddle.goto(-350,0)

rightpaddle= t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=8,stretch_len=0.5)
rightpaddle.penup()
rightpaddle.goto(350,0)

ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("SCORE", align="center",font=("MS Sans Serif",24,"normal"))



def leftpaddleup():
    y= leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

def leftpaddledown():
    y= leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)

def rightpaddleup():
    y= rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)

def rightpaddledown():
    y= rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)

window.listen()
window.onkeypress(leftpaddleup,"w")
window.onkeypress(leftpaddledown,"s")
window.onkeypress(rightpaddleup,"Up")
window.onkeypress(rightpaddledown,"Down")

while True:
    window.update()

    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)


    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        playerAscore=playerAscore + 1
        pen.clear()
        pen.write("PLAYER A: {}        PLAYER B: {}".format(playerAscore,playerBscore),align="center",font=("MS Sans Serif",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        playerBscore=playerBscore + 1
        pen.clear()
        pen.write("PLAYER A: {}        PLAYER B: {}".format(playerAscore,playerBscore),align="center",font=("MS Sans Serif",24,"normal"))

    if (ball.xcor()>340)and(ball.xcor()<350)and(
          ball.ycor()<rightpaddle.ycor()+80 and ball.ycor()>rightpaddle.ycor()-80):
        ball.setx(340)
        ballxdirection=ballxdirection* -1
    if (ball.xcor()<-340)and(ball.xcor()>-350)and(
          ball.ycor()<leftpaddle.ycor()+80 and ball.ycor()>leftpaddle.ycor()-80):
        ball.setx(-340)
        ballxdirection=ballxdirection* -1
    if leftpaddle.ycor()>300:
        leftpaddle.sety(300)
    if leftpaddle.ycor()<-300:
        leftpaddle.sety(-300)
    if rightpaddle.ycor()>300:
        rightpaddle.sety(300)
    if rightpaddle.ycor()<-300:
        rightpaddle.sety(-300)