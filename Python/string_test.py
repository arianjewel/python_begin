'''str='a quick brown fox jumps over the lazy dog'
for c in'abcdefghijklmnopqrstuvwxyz':
    print(c,str.count(i))'''
'''country='north Korea'
new_country=country.replace('north','North')
print(new_country)'''
'''text='I am a programmer. I wanna be a good programmer. I wanna better. '
new_text=text.replace('I','He')
new_text2=new_text.replace('He am','He is')
print(text)
print(new_text)
print(new_text2)'''
'''str=input()
capital='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small='abcdefghijklmnopqrstuvwxyz'
digit='0123456789'
extra='!,.?\'\"'
up=''
lo=''
dig=''
ex=''
for i in str:
    for c in capital:
        if i==c:
            up+=i
print(up)
for i in str:
    for c in small:
        if i==c:
            lo+=i
print(lo)
for i in str:
    for c in digit:
        if i==c:
            dig+=i
print(dig)
for i in str:
    for c in extra:
        if i==c:
            ex+=i
print(ex)'''
str=input()
str=str.lower()
new_str=''.join(reversed(str))
if new_str==str:
    print('Polindrome')
else:
    print('Non Polindrome')
