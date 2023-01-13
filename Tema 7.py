'''
ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
'''
'''
INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
'''
'''
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
'''
from abc import abstractmethod, ABC


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(self):
        print("Cel mai probabil am colturi")

class Patrat(FormaGeometrica):

    def __init__(self,latura):
        self.__latura = latura

    def aria(self):
        return self.__latura * self.__latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def color(self):
        print(f'Getter: latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def color(self, latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def color(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza cercului este: {self.__raza}')
        return self.__raza
    @raza.setter
    def raza(self):
        print(f'Raza cercului este: {self.__raza}')

    @raza.setter
    def raza(self, raza):
        print(f'Noua valoare a razei este: {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Am sters valoarea razei')
        self.__raza = 0

    def aria(self):
        aria_cercului = self.PI * self.__raza * self.__raza

    def descrie(self):
        print(f'Eu nu am colturi')




