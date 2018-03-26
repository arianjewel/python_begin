'''while True:
    n=int(input('please, Enter a number (0 to exit): '))
    if n==0:
        break
    if n<0:
        print('only allow positive number. please, try again.')
        continue
    print("square of",n,'=',n*n)'''
terminate_program=False
while not terminate_program:
    operation=input('please, press add/sub or quit to exit: ')
    if operation=='quit':
        break
    elif operation not in ['add','sub']:
        print("unknown operation!")
        continue
    else:
        num1=int(input('please, Enter a number: '))
        num2=int(input('please, Enter another number: '))
    while True:
        if operation=='add':
            print('Result is',num1+num2)
            break
        else:
            print('Result is',num1-num2)
            break
