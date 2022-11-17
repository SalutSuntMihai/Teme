#1
def suma(a,b):
    return a+b
print(suma(7,8))
#2
def par_sau_impar(numar):
    if numar%2==0:
        return True
    else:
        return False
print(par_sau_impar(6))
#3
def nume_complet(nume):
    nume=nume.replace(' ', '')
    nume=nume.replace('-', '')
    return len(nume)
print(nume_complet('laurentiu pastravaru'))
#4
def aria_dreptunghiului(lungime,latime):
    return lungime*latime
print(aria_dreptunghiului(7,8))
#5
PI = 3.141592653589793
def aria_cercului(raza):
    return PI*raza**2
print(aria_cercului(7))
#6
def in_range(string):
    x=str(input('Introduceti caracter: '))
    if x in string:
        return True
    else:
        return False
print(in_range('Gassdsasdsdsdssaaaaaaaa'))
#7
def upper_lower(string):
    upper=0
    lower=0
    for i in range(len(string)):
        if string[i].islower():
            lower = lower+1
        elif string[i].isupper():
            upper = upper+1
    print(f'lower {lower}')
    print(f'upper {upper}')
upper_lower('JJASsssss')
#8
def lista_poz(lista_numere):
    lista_numere_poz = []
    for numar in lista_numere:
        if numar >= 0:
            lista_numere_poz.append(numar)
    return lista_numere_poz
#9
def comparator1(x, y):
    if x == y:
        print('Numerele sunt egale!')
    elif x > y:
        print(f'{x} este mai mare decat {y}!')
    else:
        print(f'{y} este mai mare decat {x}!')
#10
def set_nr(nr, set_numere):
    if nr in set_numere:
        print("Printeaza ‘nu am adaugat numarul in set. Acesta exista deja")
        return False
    else:
        set_numere.add(nr)
        print('Am adaugat numarul nou in set!')
        return True




