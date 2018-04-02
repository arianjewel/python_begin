'''def is_prime1(n):
    if n<2:
        return False
    prime=True
    str1=''
    li=[]
    for x in range(2,n):
        if n%x==0:
            x=str(x)
            li.append(x)
            prime=False
    str1=','.join(li)
    if str1!='':
        print(n,'is divisible by',str1)
    return prime
while True:
    number=int(input('please enter a number (enter 0 to exit): '))
    if number==0:
        break
    prime=is_prime1(number)
    if prime is True:
        print(number,'is a prime number.')
    else:
        print(number,'is not a prime number')'''




#efficient
'''def is_prime2(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    m=n//2+1
    for x in range(3,m,2):
        if n%x==0:
            return False
            break
    return True
while True:
    input_number=int(input('please enter a number (0 to exit): '))
    if input_number==0:
        break
    prime=is_prime2(input_number)
    if prime is True:
        print(input_number,'is a prime number.')
    else:
        print(input_number,'is not a prime number.')'''




#more efficient
'''import math
def is_prime3(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    m=int(math.sqrt(n))
    m+=1
    for x in range(3,m,2):
        if n%x==0:
            return False
            break
    return True
while True:
    input_number=int(input('please enter a number (0 to exit): '))
    if input_number==0:
        break
    prime=is_prime3(input_number)
    if prime is True:
        print(input_number,'is a prime number.')
    else:
        print(input_number,'is not a prime number.')'''




#is_prime2 & is_prime3 check with timeit.....which is efficient
import math
def is_prime3(n=1013):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    m=int(math.sqrt(n))
    m+=1
    for x in range(3,m,2):
        if n%x==0:
            return False
            break
    return True
def is_prime2(n=1013):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    m=n//2+1
    for x in range(3,m,2):
        if n%x==0:
            return False
            break
    return True
import timeit
t1=timeit.timeit(is_prime2)
t2=timeit.timeit(is_prime3)
print(t1,t2,t1/t2)
