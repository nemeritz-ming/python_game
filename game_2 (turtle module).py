import turtle
import os
import winsound
wn = turtle.Screen()
wn.title("game_2 turtle module")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# main game loop
# score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # 5 times width
paddle_a.penup()
paddle_a.goto(-350, 0)
# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # 5 times width
paddle_b.penup()
paddle_b.goto(350, 0)
# ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx= 0.1
ball.dy= 0.1
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
# hide
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A: 0 player B: 0", align= "center", font= ("courier", 24, "normal"))
# paddle movement
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
# ball movement
# keyboard binding
wn.listen() # listen for keyborad input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
while True:
    wn.update()  # every time the loop runs, it will update the screen

    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # boarder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # add music   winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    # add music   os.system("afplay bounce.wav")  # on mac is os.system("aplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    #  for more collition
    #if ball.xcor() > 390:
    #    ball.setx(390)
    #   ball.dx *= -1
    #if ball.xcor() < -390:
    #    ball.setx(-390)
    #    ball.dx *= -1
    #  when one lose, reset the ball and change the direction
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *=1
        score_a +=1
        pen.clear()
        pen.write("player A: {} player B: {}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *=1
        score_b += 1
        pen.clear()
        pen.write("player A: {} player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    # paddle and ball collision
    if ball.xcor() > 338 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(338)
        ball.dx *= -1
    if ball.xcor() < -338 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-338)
        ball.dx *= -1

