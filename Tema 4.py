masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#1 a)
for x  in range(len(masini)):
    print(f'[for]Masina mea preferata este {masini[x]}')
#b)
x=0
while x<=len(masini)-1:
    print(f'[while]Masina mea preferata este {masini[x]}')
    x = x + 1
#c)
for m in masini:
    print(f'[for each]Masina mea preferata este '+ m)
#2
for i in range(1,len(masini)-1):
    masini[i]=masini[i].upper()
    print(masini)
#3
for masina in masini:
    if  masina=='MERCEDES':
        print(f'Am gasit masina dorita de dvs, adica {masina}')
        break
    print(f'Am gasit masina {masina}, mai cautam')
#4
for masina_buna in masini:
    if masina_buna=='TRABANT' or masina_buna=='LASTUN':
        continue
    else:
        print(f'S-ar putea sa va placa {masina_buna}')
#5
masini_vechi=[]
for k in range(len(masini)):
    if masini[k] == 'LASTUN' or masini[k] == 'TRABANT':
        masini_vechi.append(masini[k])
        masini[k]='Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')
#6
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
'''buget= int(input('Ce buget aveti ?'))
for masina in pret_masini:
    if buget>=pret_masini[masina]:
        print(f'pentru un buget de {pret_masini[masina]} puteti achizitiona {masina}')'''
#7
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(numere)
total=0
for numar in numere:
    if numar == 3:
        total += 1
#8
suma = 0
for numar in numere:
    suma += numar
print(f'Suma tuturor elementelor este {suma}.')
#9
numar = 0
for q in numere:
    if q > numar:
        numar = q
print(f'Cel mai mare numar din lista este {numar}.')
#10
for z in range(len(numere)):
    if numere[z]<0:
        numere[z]=numere[z]*-1
print(numere)




