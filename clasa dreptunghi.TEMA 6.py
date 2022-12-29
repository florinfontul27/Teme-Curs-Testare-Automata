'''
2.
Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
Puteti verifica schimbarea culorii prin apelarea metodei descrie().

'''

class Dreptunghi:
    lungime = ""
    latime = ""
    culoare = ""

    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f'Dreptunghiul are lungimea de {self.lungime} cm,latimea de {self.latime} cm si culoarea {self.culoare}.')

    def calculeaza_aria_dreptunghiului(self,):
        self.aria = self.lungime * self.latime
        return  self.aria

    def calculeaza_perimetrul(self):
        self.perimetrul = 2 * self.lungime + 2 * self.latime
        return self.perimetrul

    def schimba_culoarea(self,culoare_noua):
        self.culoare = culoare_noua


dreptunghi1 = Dreptunghi(50,25,"rosu")
dreptunghi1.descrie_dreptunghi()
dreptunghi2 = Dreptunghi(100,50,"verde")
dreptunghi2.descrie_dreptunghi()
print(f'Aria dreptunghiului este {dreptunghi1.calculeaza_aria_dreptunghiului()}')
print(f'Aria dreptunghiului este {dreptunghi2.calculeaza_aria_dreptunghiului()}')
print(f'Perimetrul dreptunghiului este {dreptunghi1.calculeaza_perimetrul()}')
print(f'Perimetrul dreptunghiului este {dreptunghi2.calculeaza_aria_dreptunghiului()}')
dreptunghi1.schimba_culoarea("maro")
print(f'Noua culoare a dreptunghiului este {dreptunghi1.culoare}.')
dreptunghi2.schimba_culoarea("gri")
print(f'Noua culoare a dreptunghiului este {dreptunghi2.culoare}.')










