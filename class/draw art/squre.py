import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")
    #Create the turtle brad- Draws a square
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)
    #Create the turtle pit- Draws a circle
    #pit = turtle.Turtle()
    #pit.shape("arrow")
    #pit.color("blue")
    #pit.circle(100) '''
    
    window.exitonclick()

draw_art()

'''
I wrote this at first to make circle from square
angle=0
    while(angle<360):
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.right(5)
        angle+=5 '''
