import turtle

prev=0
start=1
fibno=1
sqs = input("How many Squares do you want? ")
for i in range(int(sqs)):
   # Show numbers to make sure things are correct...
   print(str(i+1)+". "+str(fibno))

   # Draw a square
   turtle.color('red')
   for f in range(6):
       turtle.forward(5*fibno)
       if f<5:
           turtle.left(90)

   # Sort out numbers
   fibno=start+prev
   prev=start
   start=fibno
turtle.done()
