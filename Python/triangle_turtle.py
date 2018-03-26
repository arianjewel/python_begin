'''import turtle
turtle.speed(3)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)
turtle.exitonclick()'''
side_length=int(input('Please, enter triangle side length size(c.m): '))
import turtle
turtle.speed(2)
turtle.color('red')
def trianle_draw(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)
trianle_draw(side_length)
turtle.exitonclick()
