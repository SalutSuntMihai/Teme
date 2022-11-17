#1
note_muzicale=("do", "re", "mi", "fa", "sol", "la", "si", "do")# declarare
print(note_muzicale) #afisare
varianta_inversa=note_muzicale[::-1] #declarare string invers
do_do=slice(0,8) #slice de varianta inversa dar nu stiu de ce
print(varianta_inversa[do_do]) #afisare varianta inversa cu slice
def varianta_si_mai_inversa(varianta_inversa): #definire functie pentru varianta inversa
    return varianta_inversa[::-1]
varianta_inversa = varianta_si_mai_inversa(varianta_inversa)
print(varianta_inversa)
#2
#De 6 ori
#3
a=[3,1,0,2]
b=[6,5,4]
c= a+b
a.extend(b)
print(c)
print(a)
#4
a.sort()
a.remove(0)
print(a)
#5
if len(c)==0:
    print("lista e goala")
else:
    print("lista nu e goala")
#6
c.clear()
#7
if len(c)==0:
    print("lista e goala")
else:
    print("lista nu e goala")
#8
dict1={
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
print(dict1.keys())
#9
print("Ana a luat nota "+str(dict1['Ana']))
print("Gigel a luat nota "+str(dict1['Gigel']))
print("Dorel a luat nota "+str(dict1['Dorel']))
#10
dict1['Dorel']=6
print(dict1.items())
#11
dict1.pop('Gigel')
dict1.update({'Ionica': 9})
print(dict1.keys())
#12
set
zile_sapt={'sambata','duminica'}
weekend={'sambata','duminica'}
zile_sapt.add('luni')
print(zile_sapt)
#13
if weekend.issubset(zile_sapt):
    print('weekend este subset')
else:
    print('weekend nu e subset')
#14
print(zile_sapt.difference(weekend))
#15
print(zile_sapt.intersection(weekend))