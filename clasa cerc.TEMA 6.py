'''1.
Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''

class Cerc:
    raza = ""
    culoare = ""
    pi = 3.14
    x = 2
    def __init__(self,culoare,raza):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza {self.raza}.')

    def calculeaza_aria(self):

        self.aria = self.pi*(self.raza**2)
        return self.aria

    def calculeaza_diametru(self):
        self.diametrul = self.x * self.raza
        return self.diametrul

    def calculeaza_circumferinta(self):
        self.circumferinta = self.pi * self.diametrul
        return self.circumferinta
cerc1 = Cerc("rosie",30)
cerc1.descrie_cerc()
cerc2 = Cerc("verde",40)
cerc2.descrie_cerc()
print(f'Cercul are aria {cerc1.calculeaza_aria()}')
print(f'Cercul are aria {cerc2.calculeaza_aria()}')
print(f'Cercul are diametrul {cerc1.calculeaza_diametru()}')
print(f'Cercul are diametrul {cerc2.calculeaza_diametru()}')
print(f'Cercul are circumferinta {cerc1.calculeaza_circumferinta()}')
print(f'Cercul are circumferinta {cerc2.calculeaza_circumferinta()}')



















