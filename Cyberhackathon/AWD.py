import csv 

uzytkownicy = {
    "anna_nowak": "annanowak123",
    "piotr_szymanski": "piotrszymanski123",
    "pawel_dabrowski": "paweldabrowski123",
    "wojciech_torbus": "wojciechtorbus123",
    "ola_szewczyk": "olaszewczyk123"
}                                               
liczba_prob = 3 

print("Witaj! Zaloguj się do aplikacji:")

while liczba_prob > 0:

    login = input("Login: ")
    haslo = input("Hasło: ")

    if login in uzytkownicy and uzytkownicy[login] == haslo:
        print("Zalogowano pomyślnie!")
        print("Witaj,",login,"!")
        break
    
    else:
        liczba_prob -= 1

        print("Błąd logowania. Spróbuj ponownie. Pozostało: ",liczba_prob,"prób.")
            
    
if liczba_prob == 0:
        print("Nie udało sie zalogować. Uruchom ponownie program, aby spróbować ponownie!")
        exit()

print("Aby zdać raport najpierw podaj swoje dane.")
imie = input("Imię: ")                                  #pyta o dane zgłaszającego (imie, nazwisko i nr identyfikatora)
nazwisko = input("Nazwisko: ")
identyfikator = input("Numer identyfikatora(XXXX): ")
while len(identyfikator)!= 4:
    print("Identyfikator powininen składać się z 4 cyfr!")
    identyfikator = input("Podaj ponownie numer identyfikatora: ")
    if len(identyfikator) == 4:
        break


print("")       #linia przerwy


data = input("Kiedy doszło do wypadku (DD-MM-RRRR): ")                  #podanie daty wypadku
while len(data) != 10:
    print("Proszę o wpisanie daty według podanego wzoru!")
    data = input("Podaj ponownie kiedy doszło do wypadku(DD-MM-RRRR): ")
    if len(data) == 10:
        break 
print("")       #linia przerwy
miejsce = input("Gdzie zdarzenie miało miejsce: ")           #podanie miejsca wypadku
print("")       #linia przerwy

opis = input("Proszę opisać jak doszło do wypadku oraz co się stało: ")     #opisz wypadek
print("")       #linia przerwy

swiadkowie = input("Czy w miejscu zdarzenia byli obecni inni świadkowie ('tak' lub 'nie'): ")       #pyta o świadków zdarzenia
if swiadkowie.lower() == "tak":                                                       #jeżeli byli to : pytaj dalej
    print("Postępuj dalej z instrukcjami.")
    print("")       #linia przerwy

elif swiadkowie.lower() == "nie":                                                     #jeżeli nie było: pytaj dalej
    print("Postępuj dalej z instrukcjami.")

else:                                                                                #jeżeli inna odpowiedź...
    while swiadkowie.lower() != "tak" or "nie":
        print("Błędne dane. Sprawdź, czy dobrze odpowiedziałeś na pytanie!!!   'tak' lub 'nie'   ")     #błędne dane: sprawdź i podaj jeszcze raz
        swiadkowie = input("Czy w miejscu zdarzenia byli obecni inni świadkowie ('tak' lub 'nie'): ")       #pyta o świadków zdarzenia

        if swiadkowie.lower() == "tak":                                                       #jeżeli byli to : pytaj dalej
            print("Postępuj dalej z instrukcjami.")
            print("")       #linia przerwy

        elif swiadkowie.lower() == "nie":                                                     #jeżeli nie było: pytaj dalej
            print("Postępuj dalej z instrukcjami.")
            break               
                
print("")               #dalsze pytania po poprawnej odpowiedzi ('tak' lub 'nie')

urazy = input("Czy pracownik lub inne osoby odniosły urazy w wyniku wypadku ('tak' lub 'nie'): ")
if urazy.lower() == "tak":
    print("Postępuj dalej z instrukcjami.")

elif urazy.lower() == "nie":
    print("Postępuj dalej z instrukcjami.")
else:
    while urazy.lower() != "tak" or "nie":
        print("Błędne dane. Sprawdź, czy dobrze odpowiedziałeś na pytanie!!!   'tak' lub 'nie'   ")
        urazy = input("Czy pracownik lub inne osoby odniosły urazy w wyniku wypadku ('tak' lub 'nie'): ")

        if urazy.lower() == "tak":
            print("Postępuj dalej z instrukcjami.")
            break
            print("")       #linia przerwy

        elif urazy.lower() == "nie":
           print("Postępuj dalej z instrukcjami.")
           break
        
print("")

uwagi = input("Czy istnieją jakiekolwiek dodatkowe uwagi lub informacje, które należy uwzględnić? ('tak' lub 'nie'):")
if uwagi == "tak":
    uwagi_jakie = input("Podaj jakie: ")

elif uwagi == "nie":
    uwagi_jakie = "nie"
    
else:
    while uwagi != "tak" or "nie":
        print("Błędne dane. Sprawdź, czy dobrze odpowiedziałeś na pytanie!!!   'tak' lub 'nie'   ")
        uwagi = input("Czy istnieją jakiekolwiek dodatkowe uwagi lub informacje, które należy uwzględnić? ('tak' lub 'nie'):")
        print("")
        if uwagi == "tak":
            uwagi_jakie = input("Podaj jakie: ")
            break

        elif uwagi == "nie":
            uwagi_jakie = "nie"
            break

print("")

print("Dziękujemy za wypełnienie formularza dot. wypadku.")

    
        
with open ('dane.csv',mode='w') as danecsv:
    pola = ['Imię','Naziwsko','Identyfikator','Data','Miejsce','Opis','Świadkowie','Urazy','Uwagi']
    lista = [{'Imię':imie.capitalize(),'Naziwsko':nazwisko.capitalize(),'Identyfikator':identyfikator.capitalize(),'Data':data.capitalize(),'Miejsce':miejsce.capitalize(),'Opis':opis.capitalize(),'Świadkowie':swiadkowie.capitalize(),'Urazy':urazy.capitalize(),'Uwagi':uwagi_jakie.capitalize(),}]
    writer = csv.DictWriter(danecsv, fieldnames=pola)
    writer.writeheader()
    for x in lista:
        writer.writerow(x)

with open ('dane.csv') as danecsv:
    czytnikCSV = csv.reader(danecsv,delimiter=";")
