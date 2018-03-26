'''import turtle
turtle.shape('arrow')
turtle.speed(3)
for n in range(5):
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)
    if n==4:
        break
    turtle.penup()
    turtle.forward(55)
    turtle.pendown()
turtle.exitonclick()'''
import turtle
turtle.speed(5)
turtle.color('blue')
def square_draw(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)
counter=0
while counter<90:
    square_draw(100)
    turtle.right(4)
    counter+=1
turtle.exitonclick()
