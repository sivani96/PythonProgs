import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(50)
        some_turtle.right(90)

def draw_shape():
    window=turtle.Screen()
    window.bgcolor("black")

    boo=turtle.Turtle() 
    boo.shape("turtle")
    boo.speed(3)
    boo.color("green")

    for i in range(1,37):
        draw_square(boo)
        boo.right(10)



    window.exitonclick()
    
draw_shape()
