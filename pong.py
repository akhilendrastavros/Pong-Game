import turtle as t
playerAscore = 0
playerBscore = 0

window=t.Screen()
window.title("PONG")
window.bgcolor("cyan")
window.setup(width=800,height=600)
window.tracer(0)

bar1= t.Turtle()
bar1.speed(0)
bar1.shape("square")
bar1.color("white")
bar1.shapesize(stretch_wid=8,stretch_len=0.5)
bar1.penup()
bar1.goto(-350,0)

bar2= t.Turtle()
bar2.speed(0)
bar2.shape("square")
bar2.color("white")
bar2.shapesize(stretch_wid=8,stretch_len=0.5)
bar2.penup()
bar2.goto(350,0)

ball = t.Turtle()
ball.speed(0)
ball.shape("triangle")
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



def bar1up():
    y= bar1.ycor()
    y=y+90
    bar1.sety(y)

def bar1down():
    y= bar1.ycor()
    y=y-90
    bar1.sety(y)

def bar2up():
    y= bar2.ycor()
    y=y+90
    bar2.sety(y)

def bar2down():
    y= bar2.ycor()
    y=y-90
    bar2.sety(y)

window.listen()
window.onkeypress(bar1up,"w")
window.onkeypress(bar1down,"s")
window.onkeypress(bar2up,"Up")
window.onkeypress(bar2down,"Down")

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
          ball.ycor()<bar2.ycor()+80 and ball.ycor()>bar2.ycor()-80):
        ball.setx(340)
        ballxdirection=ballxdirection* -1
    if (ball.xcor()<-340)and(ball.xcor()>-350)and(
          ball.ycor()<bar1.ycor()+80 and ball.ycor()>bar1.ycor()-80):
        ball.setx(-340)
        ballxdirection=ballxdirection* -1
    def barinscreen():
        if bar1.ycor()>300:
            bar1.sety(300)
        if bar1.ycor()<-300:
            bar1.sety(-300)
        if bar2.ycor()>300:
            bar2.sety(300)
        if bar2.ycor()<-300:
            bar2.sety(-300)
    def changegamescene():
        if (playerAscore > 3) or (playerBscore > 3):
            ball.shape("circle")
            ball.color("red")
            bar1.color("red")
            bar2.color("red")

        

    barinscreen()
    changegamescene()
