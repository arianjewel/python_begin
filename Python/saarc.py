'''saarc=[0]*7
for i in range(7):
    saarc[i]=input()
print(saarc)'''
'''saarc=['Bangladesh','India','Pakistan','Srilanka','Bhutan','Nepal','Afganistan']
country=input("Enter the name of the country: ")
if country in saarc:
    print(country,"is a member of saarc")
else:
    print(country,"is not a member of saarc")
print('program copmlete on cmd')'''
saarc=[]
while True:
    i=input('please input saarc country name or write stop for end: ')
    if i=='stop':
        break
    else:
        saarc.append(i)
while True:
    text=input('please input which mode you want(ascending or descending): ')
    text=text.lower()
    if text=='ascending':
        saarc.sort()
        break
    elif text=='descending':
        saarc.sort()
        saarc.reverse()
        break
    else:
        print('please write ascending or descending')
print(saarc)
