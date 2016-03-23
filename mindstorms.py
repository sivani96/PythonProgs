import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(50)
        some_turtle.right(90)

def draw_shape():
    window=turtle.Screen()
    window.bgcolor("black")

    boo=turtle.Turtle() #calling init() method of Turtle class
    boo.shape("turtle")
    boo.speed(3)
    boo.color("green")

    for i in range(1,37):
        draw_square(boo)
        boo.right(10)

    #andy=turtle.Turtle()
    #andy.shape("arrow")
    #andy.speed(3)
    #andy.color("blue")
    #andy.circle(50)

    #nimbo=turtle.Turtle()
    #nimbo.shape("circle")
    #nimbo.color("red")

    #i=0
    #while(i<3):
     #   nimbo.forward(50)
      #  nimbo.right(120)
       # i=i+1
    

    window.exitonclick()
    
draw_shape()
