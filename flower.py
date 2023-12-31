import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")

# Create a turtle for drawing
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.speed(0)  # fastest drawing speed

# Draw the stem
t.penup()
t.goto(0, -150)
t.pendown()
t.width(10)
t.goto(0, 30)  # Adjusted stem height to connect to the flower base

# Draw the base of the flower
t.penup()
t.goto(0, 30)  # Move to the top of the stem
t.pendown()
t.begin_fill()
t.color("green")  # Change color to green for the base
t.circle(30)
t.end_fill()

# Draw the petals
num_petals = 10
for _ in range(num_petals):
    t.penup()
    t.goto(0, 60)
    t.pendown()
    t.begin_fill()
    t.color("pink")  # Change the petal color
    t.circle(60, 90)
    t.left(90)
    t.circle(60, 90)
    t.left(90)
    t.end_fill()
    t.right(360 / num_petals)

# Draw smaller petals
t.width(5)
num_small_petals = 10
for _ in range(num_small_petals):
    t.penup()
    t.goto(0, 60)
    t.pendown()
    t.begin_fill()
    t.color("red")  # Change the petal color
    t.circle(40, 90)
    t.left(90)
    t.circle(40, 90)
    t.left(90)
    t.end_fill()
    t.right(360 / num_small_petals)

# Draw the center of the flower
t.penup()
t.goto(0, 60)
t.pendown()
t.color("brown")
t.dot(30)

# Hide the turtle and display the drawing
t.hideturtle()
turtle.done()
