'''def myfnc(x)
    print('inside myfnc',x)
    x=10
    print('inside myfnc',x)
x=20
myfnc(x)
print(x)'''
'''def myfnc(x,y,z=10):
    print('x=',x,'y=',y,'z=',z)
x=5
y=6
z=7
myfnc(x,y,z)
myfnc(x,y)'''
'''def myfnc(x,z,y=10):
    print('x=',x,'y=',y,'z=',z)
myfnc(x=1,y=2,z=3)
a=4
b=5
c=6
myfnc(z=a,x=c,y=b)'''
'''def add_numbers(numbers):
    result=0
    for i in numbers:
        result+=i
    return result
result=add_numbers([1,2,3,4,4,5,6])
print(result)'''
'''def my_fnc(li):
    print(li)
    li[2]=6
    print(my_list)
my_list=[1,2,3,4,5,6,7,8,9]
print('Before function call: ',my_list)
my_fnc(my_list)
print('After function call: ',my_list)'''
'''def Avarage(numbers):
    sum=0
    number=0
    for i in numbers:
        sum+=i
        number+=1
    Avarage=sum/number
    return Avarage
li=[1,2,3,4,5,6,7,8,9]
Avarage=Avarage(li)
print(Avarage)'''
def namta(number=1):
    for i in range(10):
        print(number,"x",i+1,'=',number*(i+1))
namta()
