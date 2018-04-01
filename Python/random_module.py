'''import turtle
import random
turtle.penup()
colors=['red','green','blue','yellow','orange','black','purple']
for i in range(20):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    turtle.setposition(x,y)
    i=random.randint(0,len(colors)-1)
    turtle.dot(colors[i])
turtle.done()'''



'''import random
number=random.randint(1,1000)
attemps=0
while True:
    input_number=int(input('Guess the number(between 1 to 1000) : '))
    attemps+=1
    if number==input_number:
        break
    elif number>input_number:
        print('Incorrect! please try to guess greater than',input_number)
    else:
        print('Incorrect! please try to guess smaller than',input_number)
print('Your tried!',attemps,'times to find the correct number')
#play with user'''



import random
number=random.randint(1,1000)
low=1
high=1000
attemps=0
while True:
    print('Guess the number (between 1 to 1000)')
    input_number=(low+high)//2
    print('Your guess is',input_number)
    attemps+=1
    if number==input_number:
        print('Yeah! your guess is correct')
        break
    elif number>input_number:
        low=input_number+1
        print('Incorrect! please try to guess greater number')
    else:
        high=input_number-1
        print('Incorrect! please try to guess smaller number')
print('Your tried!',attemps,'times to find the correct number')
#play without user
