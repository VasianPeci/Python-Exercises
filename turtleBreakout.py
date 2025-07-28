import turtle

#setup the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Breakout")
screen.tracer(0)  #turn off screen updates for a better performance


#boundary variables
box_size = 400.0
boundary = box_size / 2.0

#the box
box_drawer = turtle.Turtle()
box_drawer.penup()
box_drawer.speed(0)
box_drawer.goto(-box_size / 2.0, -box_size / 2.0)
box_drawer.pendown()
box_drawer.color("hot pink")
for _ in range(4):
    box_drawer.forward(box_size)
    box_drawer.left(90)
box_drawer.hideturtle()

#paddle variables
paddle_speed = 50
paddle_width = 60.0
paddle_thickness = paddle_width / 10.0

#making the paddle
paddle = turtle.Turtle()
paddle.penup()
paddle.hideturtle()
paddle.color("hot pink")
paddle.shape("square")
paddle.shapesize(paddle_thickness/20.0, paddle_width / 20.0)
paddle.goto(0, -190)
paddle.showturtle()

#paddle controls
def paddleright():
    if paddle.xcor() + (paddle_width/2)+20< boundary:
        paddle.penup()
        paddle.forward(paddle_speed)
        paddle.pendown()
screen.onkey(paddleright,'Right')
screen.listen()
def paddleleft():
    if paddle.xcor()+ (-paddle_width/2)-20 > - boundary:
        paddle.penup()
        paddle.backward(paddle_speed)
        paddle.penup()
screen.onkey(paddleleft,'Left')
screen.listen()


#bricks
gap_size = 20
brick_width = 35
brick_thickness = 15
#list to store bricks
bricks = []

#score variable
score = 0

def brick_row(color, y):
    global bricks
    x = -boundary + gap_size
    row = []
    for _ in range(10):
        brick = turtle.Turtle()
        brick.hideturtle()
        brick.speed(0)
        brick.color(color)
        brick.penup()
        brick.goto(x, y)
        brick.shape("square")
        brick.shapesize(brick_thickness / 20.0, brick_width / 20.0)
        brick.showturtle()
        row.append(brick)
        x += 40
    bricks.append(row)
    return row

#gen bricks
y_brick = (box_size / 2.0) - gap_size - (brick_thickness / 2.0)
row1 = brick_row("hot pink", y_brick)
row2 = brick_row("light pink", y_brick - (brick_thickness + gap_size))
row3 = brick_row("pink", y_brick - 2 * (brick_thickness + gap_size))
row4 = brick_row("beige", y_brick - 3 * (brick_thickness + gap_size))


#the ball
ball = turtle.Turtle()
ball.hideturtle()
ball.shape("circle")
ball.color("light pink")
ball.penup()
ball.speed(10)
ball.goto(0, -190)
ball.showturtle()

#boundaries
min_x, max_x = -190, 190
min_y, max_y = -190, 190
ball.dx = 5  #ball change in x direction
ball.dy = 5  #ballchange in y direction

#score display turtle
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(0, box_size / 2.0 + 20)  # Position above the game box

def move():
    global bricks, score

    x = ball.xcor() + ball.dx
    y = ball.ycor() + ball.dy

    #collision with walls
    if x < min_x or x > max_x:
        ball.dx *= -1
    if y > max_y:
        ball.dy *= -1
    if y < min_y:
        cleanup(ball, paddle, bricks)
        return

    #collision with paddle
    if (paddle.xcor() - paddle_width / 2.0) <= x <= (paddle.xcor() + paddle_width / 2.0) and y <= (paddle.ycor() + 10):
        ball.dy *= -1

    #collision with bricks
    for row in bricks:
        for brick in row:
            if brick.distance(ball) < 20:
                brick.hideturtle()
                row.remove(brick)
                score += 10  # +points when destroying a brick
                ball.dy *= -1  #reverse direction when hitting a brick
                break

    ball.goto(x, y)
    screen.update()

    #checking if all bricks are eliminated
    if all(not row for row in bricks):
        cleanup_win(ball, paddle, bricks)
        return

    #display score
    draw_score()

    screen.ontimer(move, 20)

def draw_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Times New Roman", 18, "normal"))

def cleanup(ball, paddle, bricks):
    #delete ball
    ball.hideturtle()
    del ball

    #delete paddle
    paddle.hideturtle()
    del paddle

    #delete bricks
    for row in bricks:
        for brick in row:
            brick.hideturtle()
    bricks.clear()  #clears the bricks

    screen.clear()  #clears the whole screen
    screen.bgcolor("red")
    turtle.hideturtle()
    turtle.color("white")
    turtle.write("You lose!", align="center", font=("Helvetica", 30, "normal"))

def cleanup_win(ball, paddle, bricks):
    #delete ball
    ball.hideturtle()
    del ball

    #delete paddle
    paddle.hideturtle()
    del paddle

    screen.clear()  #clears the whole screen
    turtle.hideturtle()
    screen.bgcolor("green")
    turtle.color("white")
    turtle.write("You won!!", align="center", font=("Helvetica", 30, "normal"))

#start the move function
move()
screen.exitonclick()
