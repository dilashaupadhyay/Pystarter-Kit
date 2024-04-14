import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")

# Create a turtle for drawing
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.speed(0)  # fastest drawing speed

# Draw the stem (now green)
t.penup()
t.goto(0, -150)
t.pendown()
t.width(10)
t.color("green")  # Change stem color to green
t.goto(0, 30)

# Draw the base of the flower (now green)
t.penup()
t.goto(0, 30)  # Move to the top of the stem
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

# Draw the petals (now shades of red)
num_petals = 10
for _ in range(num_petals):
    t.penup()
    t.goto(0, 60)
    t.pendown()
    t.begin_fill()
    t.color("pink")
    t.circle(60, 90)
    t.left(90)
    t.circle(60, 90)
    t.left(90)
    t.end_fill()
    t.right(360 / num_petals)

# Draw smaller petals (now shades of red)
t.width(5)
num_small_petals = 10
for _ in range(num_small_petals):
    t.penup()
    t.goto(0, 60)
    t.pendown()
    t.begin_fill()
    t.color("red")
    t.circle(40, 90)
    t.left(90)
    t.circle(40, 90)
    t.left(90)
    t.end_fill()
    t.right(360 / num_small_petals)

# Draw the center of the flower with grains
t.penup()
t.goto(0, 60)
t.pendown()
t.color("orange")
t.dot(30)


# Hide the turtle and display the drawing
t.hideturtle()
turtle.done()
