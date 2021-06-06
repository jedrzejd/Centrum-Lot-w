import os #czyszczenie ekranu w pythonie
#tu bedzie trzeba importowac wszysko
wejscie=1
przejscie=1
while(wejscie!=0):
    if(przejscie==1):
        print("""Witaj w SYSTEMIE REZERWACJI BILETÓW!!
Razem z naszą aplikacją pomożemy Ci załatwić wszystkie obowiązki związane z rezerwacją biletów lotniczych.""")
   #moze jeszcze cos z trasami lotnisk zrobic, nie wiem co o tym myslisz
    #w sumie mozna ale nie wiem co z tymi trasami moznaby było zrobic
    # a i cos z zapisywaniem danych na dysk trzeba zrobic(i odczytywanie w sumie tez)
    #i jak czyscic ekran konsoli w tym pythonie smierdzacym
    print("""1. Zarządzaj lotniskiem
2. Zarządzaj samolotem
3. Zarządzaj klientem
4. Zarządzaj trasami
5. Zarządzaj biletem
0. Zakończ program
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
    #w c da sie zrobic switch ale niew iemjak to jest w pythonie wiec zrobie na if-ach
    przejscie+=1
    wybor=input()

    if(wybor=="0"):
        print("Do zobaczenia!")
        break

    if(wybor=="1"):
        print("""1. Wyświetl liste lotnisk
2. Wyświetl ilosc lotnisk w bazie
3. Usuń wybrane lotnisko
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
        lotniskowywybor=input()
        if(lotniskowywybor=="1"):
            print("tu sie wypisze lista lotnisk")
        if(lotniskowywybor=="2"):
            print("tu sie wypisze ilosc lotnisk")
        if(lotniskowywybor=="3"):
            print("tu sie usunie lotnisko")


    if(wybor=="2"):
        print("""1. Wyświetl liste samolotów
2. Wyświetl ilosc samolotów w bazie
3. Usuń wybrany samolot
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
        samolotowywybor = input()
        if (samolotowywybor == "1"):
            print("""1.Lista zajętych samolotów
2.Lista wolnych samolotów
3.Lista wszystkich samolotów
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
            jakalista=input()
            if(jakalista=="1"):
                print("wypisuje liste zajetych samolotow")
            if(jakalista=="2"):
                print("wypisuje liste wolnych samolotow")
            if(jakalista=="3"):
                print("wypisuje liste wsyzstkich samolotow")
        if (samolotowywybor == "2"):#mozna podzielić na ilosc zajetych/wolncyh/wszystkich samolotow
            print("tu sie wypisze ilosc samolotow")
        if (samolotowywybor == "3"):#trzeba wybrac samolot i go usunac(wczytanie i usuniecie)
            print("tu sie usunie samolot")

    if(wybor=="3"):
        print("""1. Wyświetl listę osób
2. Dodaj osobę
3. Usuń osobę
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
        coosoba=input()
        if(coosoba=="1"):
            print("Listaosob:")
        if(coosoba=="2"):
            print("Dodawanie osoby:")
        if(coosoba=="3"):
            print("Usuwanie osoby:")

    if(wybor=="4"):
        print("cos z trasami")

    if(wybor=="5"):
        print("""1. Wyświetl listę biletów
2. Dodaj bilet
3. Usuń bilet
Aby dokonać wyboru naciśnij odpowiedni klawisz: """)
        cobilet = input()
        if (cobilet == "1"):
            print("Listaosob:")
        if (cobilet == "2"):
            print("Dodawanie osoby:")
        if (cobilet == "3"):
            print("Usuwanie osoby:")

    for i in range(10):
        print("\n")