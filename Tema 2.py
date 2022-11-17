# 1
# if/else este o portiune de cod care da o conditie de intrare si una sau mai multe conditii de iesire
# 2
x = int(input("Introduceti numarul: "))
if x >= 0:
    print("Acest numar este natural")
elif x <= 0:
    print("Acest numar nu este natural")
else:
    pass
# 3
x = int(input("introduceti numarul"))
if x > 0:
    print("numar pozitiv")
elif x == 0:
    print("numar neutru")
else:
    print("numar negativ")
# 4
numere = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = int(input("numarul: "))
if x in numere:
    print("succes")
else:
    print("mai incearca")
# 5
x = int(input("primul numar"))
y = int(input("al doilea numar"))
c = x - y
if c > 5:
    print("diferenta mai mare de 5")
elif c > 5:
    print("diferenta mai e mai mare de 5")
else:
    print("diferneta nu este mai mare")

# 6
l = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 151, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
x = int(input("numar: "))
if x not in l:
    print("numarul nu este")
else:
    print("numarul este ")
# 7
x = int(input("primul numar: "))
y = int(input("al doilea numar: "))
if x == y:
    print("numerele sunt egale")
elif x > y:
    print("primul numar este mai mare")
else:
    print("al doilea numar este mai mare")
# 8
x = int(input("latura:"))
y = int(input("latura:"))
z = int(input("latura:"))
if x == y == z:
    print('triunghiul este echilateral')
elif x == z and z == x:
    print("triunghiul este isoscel")
elif y == z and z == y:
    print("triunghiul este isoscel")
elif x == y and y == x:
    print("triunghiul este isoscel")
else:
    print("triunghiul este oarecare")
# 9
vocale = ("a", "e", "i", "o", "u", "ă", "â")
litera = str(input("introdu litera: "))
if litera in vocale:
    print("aceasta este o vocala")
else:
    print("aceasta este o consoana")
# 10
x = int(input("nota: "))
if x <= 4:
    print("F")
elif x > 9:
    print("A")
elif x > 8:
    print("B")
elif x > 7:
    print("C")
elif x > 6:
    print("D")
elif x > 4:
    print("E")
else:
    pass
