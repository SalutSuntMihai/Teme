class Cerc:
    Pi=3.14
    def __init__(self,raza,culoare):
        self.raza=raza
        self.culoare=culoare
    def descrie_cerc(self):
        print(f'Raza cercului este {self.raza} iar culoarea este {self.culoare}')
    def aria(self):
        print(f'Aria cercului este {self.raza*self.raza*self.Pi}')
    def diametru(self):
        print(f'Diametrul cercului este {self.raza+self.raza}')
    def perimetru(self):
        print(f'Perimetrul cercului este {2*self.Pi*self.raza}')
cerc1=Cerc(3,"rosu")
cerc1.descrie_cerc()
cerc1.aria()
cerc1.diametru()
cerc1.perimetru()
class Dreptunghi:
    def __init__(self,lungime,latime,culoare):
        self.lungime=lungime
        self.latime=latime
        self.culoare=culoare
    def descriere(self):
        print(f'Dreptunghiul are culoarea {self.culoare} si are latimea {self.latime} si lungimea {self.lungime}')
    def aria(self):
        print(f'Dreptunghiul are aria egala cu {self.latime*self.lungime}')
    def perimetru(self):
        print(f'Dreptunghiul are perimetrul {2*self.lungime+2*self.latime}')
    def schimbare_culoare(self,culoare_noua):
        self.culoare=culoare_noua
dreptunghi1=Dreptunghi(4,2,"albastru")
dreptunghi1.descriere()
dreptunghi1.aria()
dreptunghi1.perimetru()
dreptunghi1.schimbare_culoare("negru")
dreptunghi1.descriere()
class Angajat:
    def __init__(self,nume,prenume,salariu):
        self.nume=nume
        self.prenume=prenume
        self.salariu=salariu
    def descriere(self):
        print(f'Angajatul are numele {self.nume} {self.prenume} si are salariul de {self.salariu} lei pe luna')
    def nume_complet(self):
        print(f'Numele complet este {self.nume} {self.prenume}')
    def salariu_lunar(self):
        print(f'Salariul lunar este {self.salariu}')
    def salariu_anual(self):
        print(f'Salariul anual este {12*self.salariu}')
    def marire_salariu(self,procent):
        print(f'Salariul lunar a fost marit la {((procent/100)*self.salariu)+self.salariu}')
angajat1=Angajat("Albert",'Einstein',2000)
angajat1.marire_salariu(50)
class Cont:
    def __init__(self,iban,titular_cont,sold):
        self.iban=iban
        self.titular_cont=titular_cont
        self.sold=sold
    def afisare_sold(self,cont):
        print(f'Titularul {self.titular_cont} are in contul {cont} {self.sold} lei')
    def debitare_cont(self,suma_debitata):
        print(f'Contul a fost debitat cu {suma_debitata} soldul este acum {suma_debitata+self.sold}')
    def creditare_cont(self,suma_creditata):
        print(f'Contul a fost creditat cu {suma_creditata} soldul este acum {self.sold-suma_creditata}')
contul1=Cont('RO200022233','Albert Einstein',200)
contul1.creditare_cont(22)
contul1.afisare_sold('Contul1')