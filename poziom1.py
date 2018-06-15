import random
import klasy
import funkcje
import main

rooms = {

    'Lecznica': {'południe': 'Dziedziniec',
            },

    'Dziedziniec': {'wschód': 'Dom Faendala',
                    'południe': 'Siedziba Towarzyszy',
                },

    'Dom Faendala': {'zachód': 'Dziedziniec',

                    },

    'Siedziba Towarzyszy': {'północ': 'Dziedziniec',
                     'wschód': 'Pole walki',

                     },

    'Pole walki': {'zachód': 'Siedziba Towarzyszy'},

}

#poziom 1, lokacja 1, lecznica
def poz1lok1():
    global currentRoom
    currentRoom = "Lecznica"
    print('''------------------------------------------------------
    POZIOM 1

    *Budzisz się obolały i zmęczony. Rozglądając się dookoła, zauważasz kobietę,
    wyglądającą na kapłankę. Nie możesz przypomnieć sobie, co się wydarzyło.*
    ------------------------------------------------------
    ''')
    print("KAPŁANKA: Witaj. Pewnie zastanawiasz się, co tutaj robisz? \n")
    answer = None
    while answer != "1" or answer != "2":
        answer = input("TY (wybierz odpowiedź): 1 - 'Tak', 2 - 'To prawda.'")
        if answer == "1" or answer == "2":
            break
    print("KAPŁANKA: Jesteś w lecznicy w Rzecznej Puszczy, ", main.hero.name, ". Wyleczyłyśmy Twoje rany, \n"
                                                                         "jednak ból minie w pełni dopiero po kilku dniach. Czy pamiętasz co się z Tobą stało?\n")
    answer = None
    while answer != "1" or answer != "2":
        answer = input("TY (wybierz odpowiedź): 1 - 'Nie.', 2 - 'Nie, powiedz mi.'")
        if answer == "1" or answer == "2":
            break
    print('''KAPŁANKA: Sama chciałabym się dowiedzieć. Trafiłeś tutaj z Helgen z głębokimi ranami. 
    Przyniósł Cię Faendal. Jeśli chcesz się dowiedzieć więcej, widziałam go niedawno na dziedzińcu.\n''')
    answer = None
    while answer != "1" or answer != "2":
        answer = input("TY (wybierz odpowiedź): \n"
                       "1 - 'Czy powiesz mi jak mogę dostać się na dziedziniec?',\n"
                       "2 - 'Czy mogę już wyjść z lecznicy?'")
        if answer == "1" or answer == "2":
            break
    print("\nKAPŁANKA: Tak. Aby wyjść z lecznicy musisz iść na południe.\n"
          "Aby iść na południe, wpisz w konsoli 'kierunek południe'")

    # ruch użytkownika do innej lokacji
    move = [None, None]
    while move[1] != "południe":
        move = input(">")
        move = move.lower().split()
        if move[1] in rooms[currentRoom]:
            # ustawianie nowego pomieszczenia w którym jest bohater
            currentRoom = rooms[currentRoom][move[1]]
            break
        # gdy nie można tam przejść
        else:
            print("Nie możesz tam iść.")

#POZIOM 2, LOKACJA 2 = dziedziniec
def poz1lok2():
    print("""
    *Jesteś na dziedzińcu w Rzecznej Puszczy. Jest to miasteczko niewielkie,
    sprawiające wrażenie przyjaznego. Niedaleko siebie widzisz niewielki targ,
    z którego słyszysz krzyczących handlowców. Zastanawiasz się, czy sprzedają oni
    leczące mikstury - przydałaby Ci się jedna. Przypominasz sobie jednak, że nie masz pieniędzy.
    Nagle słyszysz, że ktoś Cię woła.*\n""")
    print("FAENDAL: ", main.hero.name, "!!! ", main.hero.name, "!!! \n")
    print("""* Oglądasz się za siebie i widzisz Faendala, swojego znajomego.
    Przypominasz sobie, że Kapłanka mówiła, że to on cię uratował.
    """)
    answer = None
    while answer != "1":
        answer = input("TY (wybierz odpowiedź):\n "
                       "1 - 'Witaj Faednalu.' ")
        if answer == "1":
            break
    print("\nFAENDAL: Cześć, jak się czujesz? Wyzdrowiałeś już?!\n")
    answer = None
    while answer != "1" or answer != "2":
        answer = input("TY (wybierz odpowiedź):\n "
                       "1 - 'Kapłanka twierdzi, że tak.\n'"
                       "2 - 'Jeszcze trochę mnie boli.'")
        if answer == "1" or answer == "2":
            break
    print("\nFAENDAL: Muszę przyznać, że niezbyt dobrze wyglądasz... \n"
          "Chociaż zważając na to, co Cię spotkało...\n"
          "To cud, że żyjesz.\n")
    answer = None
    while answer != "1" or answer != "2":
        answer = input("TY (wybierz odpowiedź):\n "
                       "1 - 'O czym ty mówisz?', \n"
                       "2 - 'Co mnie spotkało?'\n")
        if answer == "1" or answer == "2":
            break
    print("""
    FAENDAL: Helgen zaatakował smok. To... było niesamowite.
    Wyglądało to... jakbyś wchłonął jego duszę. O takich rzeczach
    czytałem tylko w starych książkach.
    Jeśli chcesz, mogę Ci pomóc dowiedzieć się o tym
    coś więcej. Mam w domu księgę o smokach, jednak jest pewien problem.
    Aby ją przeczytać, potrzebne jest hasło.
    Jeśli chcesz, możemy spróbować ją otworzyć.
    """)
    answer = None
    while answer != "1" or answer != "2":
        answer = input("TY (wybierz odpowiedź): "
                       "1 - 'Chodźmy.', "
                       "2 - 'Gdzie mamy iść?'")
        if answer == "1" or answer == "2":
            break
    print("\nFAENDAL: Księga jest u mnie. Wpisz w konsoli 'kierunek wschód', aby przejść do mojego domu.")
    # ruch użytkownika do innej lokacji
    move = [None, None]
    while move[1] != "wschód":
        move = input(">")
        move = move.lower().split()
        if move[1] in rooms[currentRoom]:
            # ustawianie nowego pomieszczenia w którym jest bohater
            currentRoom = rooms[currentRoom][move[1]]
            break
        # gdy nie można tam przejść
        else:
            print("Nie możesz tam iść.")

# POZIOM 1, lokacja 3 - dom faendala
def poz1lok3():
    print("""*Jesteś w domu Faendala. Na ścianach znajduje się pełno
    łowieckich zdobyczy. Domyślasz się, że Faendal zajmuje się łucznictwem.
    Na końcu pomieszczenia zauważasz starą szafę. Faendal otwiera ją i wyciąga
    starą, zakurzoną księgę.*
    """)
    print("FAENDAL: Oto ona. Jak widzisz, jest to magiczna księga."
          "Aby ją otworzyć musimy zgadnąć hasło. Gotowy?\n")
    answer = None
    while answer != "1" or answer != "2":
        answer = input("TY (wybierz odpowiedź): \n"
                       "1 - 'Tak, ale mam nadzieję, że mi pomożesz?' \n"
                       "2 - 'Jestem gotowy'\n")
        if answer == "1":
            print("FAENDAL: Próbowałem wiele razy, niestety z tym zadaniem musisz poradzić sobie sam.")
            break
        if answer == "2":
            break
    print("Widzisz starą księgę. Aby ją otworzyć, musisz wpisać hasło")
    # program "odgadywanie hasła"
    password = "smoczedziecie"
    so_far = "-" * len(password)
    used = []
    while so_far != password:
        letter = input("Podaj litere:")
        print("Pobrałem: ", letter)
        if letter in password:
            print("Ta litera jest w haśle")
            new_letter = ""
            for i in range(len(password)):
                if letter == password[i]:
                    new_letter += letter
                else:
                    new_letter += so_far[i]
            so_far = new_letter
            print("\nWykorzystałeś już następujące litery:\n", used)
            print("\nNa razie zagadkowe słowo wygląda tak:\n", so_far)
        else:
            print("Tej litery nie ma w haśle.")
        if so_far == password:
            print("Odgadłeś hasło!")
            break
    print("""FAENDAL: Udało się! Daj mi chwilę, postaram się teraz poszukać
    w niej informacji o tym, kto mógłby Ci pomóc.

    *mija 10 minut*

    Z tego co widzę, o tzw. Smoczym Dziecięciu powinni coś wiedzieć
    Siwobrodzi. Ja jednak nie wiem, gdzie można ich znaleźć. Możesz zapytać
    łuczniczki Aeli, która znajduje się w Siedzibie Towarzyszy.
    """)
    while answer != "1" or answer != "2":
        answer = input("TY (wybierz odpowiedź): \n"
                       "1 - 'Jak się tam dostanę?' \n")
        if answer == "1":
            break
    print("\nFAENDAL: Ok. Wystarczy, że wpiszesz w konsoli 'kierunek zachód', później Cię pokieruję")
    while move[1] != "zachód":
        move = input(">")
        move = move.lower().split()
        if move[1] in rooms[currentRoom]:
            # ustawianie nowego pomieszczenia w którym jest bohater
            currentRoom = rooms[currentRoom][move[1]]
            break
        # gdy nie można tam przejść
        else:
            print("Nie możesz tam iść.")

#POZIOM 1, lokacja 4
def poz1lok4():
    print("""FAENDAL: Jesteśmy z powrotem na dziedzińcu.
    Dom Towarzyszy jest na południu.
    Wpisz w konsoli 'kierunek południe'
    Tam musisz iść już sam. Do widzenia więc.
    """)
    while move[1] != "południe":
        move = input(">")
        move = move.lower().split()
        if move[1] in rooms[currentRoom]:
            # ustawianie nowego pomieszczenia w którym jest bohater
            currentRoom = rooms[currentRoom][move[1]]
            break
        # gdy nie można tam przejść
        else:
            print("Nie możesz tam iść.")
#Poziom 1, lokacja 5 - Siedziba Towarzyszy
print("""*Jesteś w Siedzibie Towarzyszy. 
Podchodzi do Ciebie mężczyzna.
""")
answer = input("KODLAK: Witaj nieznajomy. Jak Ci na imię?\n")
print("Miło mi cię poznać.\n")
answer = None
while answer != "1" or answer != "2":
    answer = input("TY (wybierz odpowiedź): \n"
    "1 - 'Kim są Towarzysze' \n"
    "2 - 'Czym zajmuje się Wasza organizacja?'")
    if answer == "2" or answer == "1":
        break
print("""\n
KODLAK: Towarzysze to grupa wojowników złożona w większości z najemników wykonujących 
różne zadania dla mieszkańców Skyrim. Dzięki temu że znaleźliśmy się w tej grupie, 
nie jesteśmy już samotni i mamy swój cel. Szanujemy bojowy hart ducha. Cenimy się nawzajem, 
jeden za drugiego oddałby życie. Swoich braci i siostry w tej wspólnej walce nazywamy Towarzyszami 
lub tarczownikami.

Nie posiadamy przywódcy, jednak ja, Kodlak Białowłosy, jestem heroldem Towarzyszy. Herold próbuje 
jedynie utrzymać Towarzyszy w jako takim porządku, aby pamiętali jaki jest ich cel nadrzędny. 
Moim poprzednikiem na tym stanowisku był Askar. Ostatnim prawdziwym przywódcą Towarzyszy 
był Ysgramor, założyciel grupy.

Powiedz mi, czego u nas poszukujesz, podróżniku?
""")
answer = None
while answer != "1":
    answer = input("TY (wybierz odpowiedź): \n"
    "1 - 'Szukam Aeli.' \n")
    if answer == "1":
        break
print("""Oczywiście. Zaraz ją zawołam.

*Po chwili podchodzi do Ciebie piękna łuczniczka. Z ciekawością zaczyna ci się przyglądać*

AELA: Dziękuję Kodlaku, porozmawiam z naszym gościem na osobności.

*Kodlak odchodzi.*

AELA: W czym mogę ci pomóc?
""")
answer = None
while answer != "1" or answer != "2":
    answer = input("TY (wybierz odpowiedź): \n"
    "1 - 'Chciałbym dowiedzieć się, gdzie znajdę Siwobrodych.' \n"
    "2 - 'Faendal powiedział mi, że wiesz, gdzie są Siwobrodzi'")
    if answer == "2" or answer == "1":
        break
print("\nAELA: Na Boga! Po cóż ich szukasz?")
answer = None
while answer != "1" or answer != "2":
    answer = input("TY (wybierz odpowiedź): \n"
    "1 - 'Nie twoja sprawa.' \n"
    "2 - 'Chcę dowiedzieć się od nich czegoś więcej o ataku smoka i moich tajemniczych umiejętnościach.'")
    if answer == "2" or answer == "1":
        break
print("""
No dobrze. Jednak takiej wiedzy nie mogę przekazać byle komu
Jeśli udowodnisz mi, że jesteś godzien posiadania tej wiedzy, 
powiem ci wszystko, co wiem. Chodź ze mną na pole walki.
Znajduje się ono na wschodzie. Wpisz 'kierunek wschód' w konsoli.""")
while move[1] != "wschód":
    move = input(">")
    move = move.lower().split()
    if move[1] in rooms[currentRoom]:
    # ustawianie nowego pomieszczenia w którym jest bohater
        currentRoom = rooms[currentRoom][move[1]]
        break
    # gdy nie można tam przejść
    else:
        print("Nie możesz tam iść.")
#Poziom 1, lokacja 6 - pole walki
def poz1lok6():
    print("""
    *Znalazłeś się na groźnie wyglądającym dziedzińcu.
    Prawdopodobnie tu Towarzysze ćwiczą swoje umiejętności.
    Aela kieruje Cię na wyznaczone miejsce.
    Ze strachem zauważasz groźnego wikołaka*

    AELA: Dobrze. Zaczynajmy więc. Twoim zadaniem jest pokonać 
    w walce tego wikołaka. Zaczynamy?
    """)
    while answer != "1" or answer != "2":
        answer = input("TY (wybierz odpowiedź): \n"
                       "1 - 'Tak.' \n"
                       "2 - 'Przepraszam, strasznie się boję. Muszę iść do toalety.'")
        if answer == "1":
            print("*Aela otwiera klatkę wilkołaka*")
            break
        elif answer == "2":
            print("AELA: Już za późno, hahaha!")
            print("*Aela otwiera klatkę wilkołaka*")
            break
    print("*Rozpoczyna się walka.")
    werewolf = Creatures()
    print("Twoje HP: ", hero.HP, "\nHP przeciwnika: ", werewolf.HP, "\n Wybierz walkę lub uleczenie się.")
    choice = None
    while choice != "walka":
        choice = input("Wpisz w konsoli: walka / leczenie")
        if choice == "walka":
            if hero.HP > werewolf.HP:
                hero.blast(werewolf)
                global fight_result
                fight_result == 1
                break
            elif hero.HP < werewolf.HP:
                hero.hero_die()
                fight_result == 0
                break
            elif hero.HP == werewolf.HP:
                print("Remis")
                fight_result == 0
        elif choice == "leczenie":
            hero.heal()
        else:
            print("Wpisałeś niewłaściwą komendę. Wpisz 'walka' lub 'ucieczka'")

    if fight_result == 1:
        print("AELA: Wspaniale, udowodniłeś, że jesteś godzien wiedzy.")
    elif fight_result == 0:
        print("""AELA: Niestety, nie udało Ci się pokonać wilkołaka. 
        Jednak udowodniłeś, że jesteś nieustraszony.""")
    print("""Siwobrodzi mieszkają na Wysokim Hrothgarze.
    Mieści się on na szczycie Gardła Świata – najwyższej góry w Tamriel.
    Wspinaczka na siedem tysięcy stopni, posiada znaczenie duchowe dla wielu Nordów, 
    ze względu na przekonania, że ludzie zostali stworzeni przez Kyne na tej górze. 
    Zachęca to do wędrówki pielgrzymów z całego Tamriel.

    Droga do Wysokiego Hrothgaru rozpoczyna się w miejscowości Ivarstead – 
    w poprzek głównego mostu w północno-zachodniej stronie wioski.
    Jeśli chcesz, zaprowadzę Cię tam.
    """)
    answer = None
    while answer != "1":
        answer = input("TY (wybierz odpowiedź): \n"
                       "1 - 'Chodźmy więc.' \n")
        if answer == "1":
            print("*AELA: Ruszamy w drogę.*")
            break

    print("""---------------------------
    Gratulacje. Ukończyłeś 1 poziom.
    ---------------------------""")
    game_state['poziom'] = 2


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")