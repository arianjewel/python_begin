row=int(input('please, Enter no of row: '))
column=int(input('please, Enter no of column: '))
import turtle
turtle.speed(3)
turtle.penup()
for i in range(column):
    for j in range(row):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*row)
    if i==column-1:
        break
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
turtle.exitonclick()
