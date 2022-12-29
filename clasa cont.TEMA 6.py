'''4.
Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''

class Cont:
    iban = ""
    titular_cont = ""
    sold = ""
    def __init__(self,iban,titular_cont,sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} de lei.')

    def debitare_cont(self):
        debitare = float(input('Treceti suma pe care vreti sa o debitati: '))
        if self.sold >= debitare:
            self.sold -= debitare
            return (f'Soldul dumneavoastra este acum {self.sold} de lei')
        else:
            return (('Fonduri insuficiente!'))

    def creditare_cont(self):
        creditare = float(input('Treceti suma pe care vreti sa o creditati: '))
        self.sold += creditare
        return (f'Soldul dumneavoastra este acum {self.sold} de lei')



cont1 = Cont("RO92BACX0002000021002002", "Ion Ionescu",12000)
cont1.afisare_sold()
cont2 = Cont("RO12BACX1112111132112114", "Marinescu Tudor",9800)
cont2.afisare_sold()
print(cont1.debitare_cont())
print(cont2.debitare_cont())
print(cont1.creditare_cont())
print(cont2.creditare_cont())



