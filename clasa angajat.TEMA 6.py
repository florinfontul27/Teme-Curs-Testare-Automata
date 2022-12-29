'''
3.
Clasa Angajat

Atribute: nume, prenume, salariu

Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''

class Angajat:
    nume = ""
    prenume = ""
    salariu = 0
    procent = 0


    def __init__(self,nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Ma numesc {self.nume} {self.prenume} si am un salariu de {self.salariu} de lei.')

    def nume_complet(self):
        return self.nume, self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self, salariu):
        self.salariu = 12 * self.salariu
        return self.salariu

    def marire_salariu(self, procent):
       self.salariu = self.salariu + procent/100*self.salariu
       return self.salariu



angajat1 = Angajat("Mihai","Stoica",3000)
angajat1.descrie()
angajat2 = Angajat("Flaviu","Popescu",3500)
angajat2.descrie()
print(f'Ma numesc {angajat1.nume_complet()}')
print(f'Ma numesc {angajat2.nume_complet()}')
print(f'Am un salariu  de {angajat1.salariu_lunar()}')
print(f'Am un salariu de {angajat2.salariu_lunar()}')
print(f'Am un salariu anual de {angajat1.salariu}')
print(f'Am un salariu anual de {angajat2.salariu}')
angajat1.marire_salariu(25)
print(f'Salariul meu a crescut la {angajat1.salariu} lei')
angajat2.marire_salariu(30)
print(f'Salariul meu a crescut la {angajat2.salariu} lei')



