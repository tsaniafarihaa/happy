import turtle
import time
import random

# Setup screen
screen = turtle.Screen()
screen.title("Happy Birthday Purwadhika!")
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Turtle for text
text_turtle = turtle.Turtle()
text_turtle.color("yellow")
text_turtle.hideturtle()
text_turtle.penup()

# Turtle for confetti
confetti_turtle = turtle.Turtle()
confetti_turtle.hideturtle()
confetti_turtle.speed(0)
confetti_turtle.penup()

# Function to display text
def display_text(message, y, font_size):
    text_turtle.goto(0, y)
    text_turtle.write(message, align="center", font=("Arial", font_size, "bold"))

# Function to create confetti effect
def confetti():
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "white"]
    for _ in range(100):
        confetti_turtle.color(random.choice(colors))
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        confetti_turtle.goto(x, y)
        confetti_turtle.dot(random.randint(10, 20))

# Animation sequence
display_text("Happy Birthday", 100, 40)
time.sleep(1)
display_text("Purwadhika!", 50, 40)
time.sleep(1)

# Add confetti
confetti()
time.sleep(3)

# Clean up
text_turtle.clear()
confetti_turtle.clear()
display_text("Wishing you a fantastic year ahead!", 0, 20)

# Hold screen
turtle.done()
