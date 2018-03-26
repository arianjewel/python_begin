year=input("enter year: ")
year=int(year)
"""if year%4!=0:
    print("this",year,"is not leap year")
else:
    if year%100==0:
        if year%400==0:
            print('this',year,"is leap year")
        else:
            print("this",year,"is not leap year")
    else:
        print('this',year,"is leap year")"""
'''if year%400==0:
    print("this",year,"is leap year")
elif year%100==0:
    print("this",year,"is not leap year")
elif year%4==0:
     print("this",year,"is leap year")
else:
     print("this",year,"is not leap year")'''
if year%100!=0 and year%4==0:
    print("this",year,"is leap year")
elif year%400==0 and year%4==0:
    print("this",year,"is leap year")
else:
    print("this",year,"is not leap year")
