# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# variabilele sunt zone din memorie care tin mai multe date

# 2. Declară și inițializează câte o variabilă din fiecare din următoarele tipuri:
# a. string
nume = 'Florin'
print(nume)

# b. int
varsta = 24
print(varsta)

# c. float
inaltime = 1.73
print(inaltime)

# d. bool
imi_place_IT = True
print(imi_place_IT)

# 3. Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.
print(type(nume))
print(type(varsta))
print(type(inaltime))
print(type(imi_place_IT))

# 4.  Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere);
# apoi verifică din nou tipul de date al acesteia.
inaltime = round(1.73)
print(inaltime)
print(type(inaltime))

# 5. Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin orice modalitate dorești (type casting, printare cu formatare).
print('Numele meu este '  + nume)
varsta = str(varsta)
print('Anul acesta am implinit varsta de ' + varsta + ' de ani.')
inaltime= str(inaltime)
print('Limita admisa in parcul pentru copii este de ' + inaltime + ' metri.')
imi_place_IT= str(imi_place_IT)
print('Am inceput cursul de testare automata pentru ' + imi_place_IT)

# 6.  Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila.
# Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'.
numele_tau= input('Care este numele tau?')
print(numele_tau)
prenumele_tau = input('Care este prenumele tau?')
print(prenumele_tau)

print(f'Numele complet are {len(numele_tau) + len(prenumele_tau)} caractere.')


# 7.
# Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila
# Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.

lungimea_dreptunghiului = int(input('Care este lungimea dreptunghiului?'))
print(lungimea_dreptunghiului)
latimea_dreptunghiului = int(input('Care este latimea dreptunghiului?'))
print(latimea_dreptunghiului)
print(f'Aria dreptunghiului este {lungimea_dreptunghiului * latimea_dreptunghiului}')

#Ex_8 - Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare cuvântul 'the' în acest string
prop ='Coral is either the stupidest animal or the smartest rock'
print(prop.count(' the '))

#EX_9 Folosindu-te de string-ul de la exercițiul 8, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”) si afișează pe ecran rezultatul
prop ='Coral is either the stupidest animal or the smartest rock'
print(f'{prop.replace("the", "THE")}')

#Ex_10 Folosindu-te de string-ul de la exercițiul 8 foloseste un assert ca să verifici dacă acest string conține doar numere.
prop ='Coral is either the stupidest animal or the smartest rock'
# assert prop.isdigit() is True, 'Propozitia nu contine doar cifre'

"""
Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai nevoie de Google)
"""
#Ex_1 Citește de la tastatură un string de dimensiune impară și afișează caracterul din mijloc.
					# Nu se va verifica daca string-ul este impar (se presupune ca vom introduce un numar corect de caractere),
							# ci doar se va printa pe ecran caracterul din mijloc.
text = str(input('Scrie un string: '))
print(f'Caracterul din mijloc este: {text[(len(text)//2)]}')

#Ex_2 Folosind assert, verifică dacă un string este palindrom.
text = 'ana'
assert text == text[::-1], 'Cuvantul nu este palindrom'

#Ex_3 - Citește de la tastatură un string care sa fie format din doua cuvinte (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.
text = str(input('Scrie un string: '))
x, y = text.split(' ')
print(f'Primul cuvant este: {x}')
print(f'Ultimul cuvant este: {y}')

#Ex_14 - Citește un string de la tastatură (ex: alabala portocala) asupra caruia sa efectuezi urmatoarele:
# salvează primul caracter într-o variabilă
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
text = str(input('Scrie un string: '))
prima_litera = text[0]
string_modificat = text[0]+text[1:len(text)-1].replace(x,x.upper())+text[len(text)-1]
print(string_modificat)

#Ex_15 - Citeste de la tastatura un user si o parola. Afiseaza pe ecran urmatoarea propizitie: 'Parola pt userul x este ***** si are x caractere'.
user = str(input('User-ul este: '))
parola = str(input('Tasteaza parola: '))
parola_ascunsa = '*' * len(parola)
print(f'Parola pentru userul {user} este {parola_ascunsa} si are {len(parola)} caractere')