import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("My first Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkingSquare(100)
shrinkingSquare(75)
shrinkingSquare(50)

turtle.done()