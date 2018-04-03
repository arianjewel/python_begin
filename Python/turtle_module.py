'''import turtle
turtle.color('red','yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.position())<1:
        break
turtle.end_fill()
turtle.done()'''



'''import turtle
r=120
a=360
turtle.circle(r,a)
turtle.done()'''



import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")

squares = input("How many squares do you want?: ")

n = 10
for sqs in range(int(squares)):
   for i in range(6):  #it has 6 turns (not 4) because the next square begins from the corner diagonal to the corner the preceding square began
      tess.forward(n)
      tess.left(90)
   tess.right(90)      #this points the turtle in the right direction to start the next square!

wn.mainloop()
