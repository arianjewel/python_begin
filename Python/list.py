'''fruits=['Apple','Mango','Banana','Orange']
fruits.append('Grape')
#print(fruits)
fruits.insert(2,'Guava')
#print(fruits)
item=input('please write Which fruits you wanna remove from list: ')
if item in fruits:
    fruits.remove(item)
    print(fruits)
else:
    print(item,'not in list')
fruits.sort()
#print(fruits)
fruits.reverse()
#print(fruits)'''



'''fruits=['Apple','Mango','Banana','Orange']
item=fruits.pop()
print(item)
print(fruits)
new_item=fruits.pop(1)
print(new_item,fruits)'''



'''li=[1,2,3]
li2=[3,4,5,6]
li.extend(li2)
#now li=[1,2,3,3,4,5,6] for extend() method
#n=li.count(3)
#print(n)
del(li[2])
#now li=[1,2,3,4,5,6] for del() method with index
del(li)
#now li is undefined for del()....... li is remove from projectself.'''



'''li1=[1,2,3]
li2=[4,5,6]
li=li1+li2
print(li)'''



'''li=[1,2,3]
li2=li*3
print(li2)'''



'''li=['a','b','c']
str=''.join(li)
#now str=abc
str=','.join(li)
#now li=a,b,c
str='-'.join(li)
#now li=a-b-c'''




li=[]
for i in range(1,11):
    li.append(i)
print(li)
