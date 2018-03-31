'''dt={} #empty dictionary
dt={1: 23,2: 34,3: 65} #multy-element dictionary'''



'''dt={}
dt[1]='one'
dt[2]='two'
dt[3]='three'
#now dt={1: 'one',2: 'two',3:'three'}'''



'''marks={'dh1001': {'bangla': 74,'english':73},'dh1002':{'bangla':70,'english':75}}
print(marks['dh1001'])
#output {'bangla': 74,'english': 73}
print(marks['dh1001']['english'])
#output 73
marks['dh1003']={'bangla': 76,'english': 67}
#now marks={'dh1001': {'bangla': 74,'english':73},'dh1002':{'bangla':70,'english':75},'dh1003':{'bangla': 76,'english': 67}}'''




'''bd_division_info={}
while True:
    i=input('please, write your division name or write stop to exit: ')
    i=i.lower()
    if i=='stop':
        break
    else:
        d=int(input('please write how much district on '+i+' division: '))
        up=int(input('please write how much upazila on '+i+' division: '))
        un=int(input('please write how much union on '+i+' division: '))
        bd_division_info[i]={'district': d,'upazila': up,'union': un}
divisions=bd_division_info.keys()
count=0
for division in divisions:
    district=bd_division_info[division]['district']
    count+=district
print('total district in bangladesh is',count)'''
