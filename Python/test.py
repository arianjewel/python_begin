'''num=input("")
num=int(num)
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")'''
'''sum=0
for i in range(1,101):
    if i%5==0:
        print(i)
        sum+=i
print(sum)'''
'''i=int(input())
j=1
while j<11:
    print(i,'x',j,'=',i*j)
    j+=1'''


n1=int(input())
for x in range(2,n1):
    if n1%x!=0:
        continue
    else:
        print('ok')
        break
