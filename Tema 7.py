from abc import abstractmethod
class FormaGeometrica:
    Pi=3.14

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print('cel mai probabil am colturi')


class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.__latura=latura

    @property
    def latura(self):
        return self.latura

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self,latura):
        self.__latura=latura
    def aria(self):
        return self.latura*self.latura

    @latura.deleter
    def latura(self):
            del self.__latura
x = Patrat(3)
print(x.aria())
x.descriere()
'''Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte 
(optional, doar daca ati ales sa implementati metoda abstracta aria)'''

class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.__raza=raza

    @property
    def raza(self):
        return self.raza

    @raza.getter
    def raza(self):
        self.__raza

    @raza.setter
    def raza(self,raza):
        self.__raza=raza
    def aria_cerc(self):
        print (self.Pi*self.__raza*self.__raza)
    @raza.deleter
    def raza(self):
        del self.__raza
Cerc(3.1).aria_cerc()


