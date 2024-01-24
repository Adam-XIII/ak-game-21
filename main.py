import random
import os
import ascii_art


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def start_menu():
    s_menu = input("New game: 'N'\nQuit game: 'Q': ")
    return s_menu

def drukuj_karty(karty):
    lista_ascii=[]
    for karta in karty:
        wybrana_karta_nazwa = karta
        wybrana_karta = getattr(ascii_art, wybrana_karta_nazwa)
        lista_ascii.append(wybrana_karta['art'])

    # Split the ASCII art strings into lines
    lines_list = [art.strip().split('\n') for art in lista_ascii]

    # Ensure all ASCII arts have the same number of lines (pad with empty lines if needed)
    max_lines = max(len(lines) for lines in lines_list)
    for lines in lines_list:
        lines.extend([''] * (max_lines - len(lines)))

    # Combine lines for each row and join rows with newlines
    karty_na_ekran = '\n'.join(''.join(lines[i] for lines in lines_list).strip() for i in range(max_lines))

    return karty_na_ekran


def dodaj_karte():
    karta = random.choice(talia)
    return karta

def wartosc_kart(karty):
    wartosc_kart_local=0
    for karta in karty:
        wybrana_karta_nazwa = karta
        wybrana_karta = getattr(ascii_art, wybrana_karta_nazwa)
        wartosc_kart_local += wybrana_karta.get('value')
    if 'aas' in karty and wartosc_kart_local > 21:
        wartosc_kart_local -= 10

    return wartosc_kart_local

def sprawdz_wynik(karty_g, karty_c):
    if karty_g == 21:
        return 'Wygrywasz! Masz BlackJacka!'
    elif karty_g > karty_c:
        return 'Wygrywasz!'
    elif karty_c > karty_g:
        return 'Przegrywasz!'
    else:
        return 'Remis?'


game_is_on = True
talia = ['dwojka', 'trojka', 'czworka', 'piatka', 'szostka', 'siodemka', 'osemka', 'dziewiatka', 'dziesiatka', 'krol', 'dama', 'dupek', 'aas']

while game_is_on:
    print(ascii_art.logo)
    s_menu = start_menu()
    if s_menu.lower() == 'n':
        cls()
        karty_gracza = []
        karty_krupiera = []

        print("game start:")
        for x in range (0, 2):
            karty_gracza.append(dodaj_karte())
            karty_krupiera.append(dodaj_karte())
            if wartosc_kart(karty_krupiera) == 21:
                print("Przegrywasz! Krupier ma BlackJacka!")

        dalszy_krok = ''
        while dalszy_krok.lower() != 'n':
            cls()
            print(f"Wartosc twoich kart: {wartosc_kart(karty_gracza)}")
            print(drukuj_karty(karty_gracza))
            print(f"Wartosc kart krupiera: {wartosc_kart(karty_krupiera)}")
            print(drukuj_karty(karty_krupiera))
            dalszy_krok = input("Co robisz?:\n'G': Dobieram karte\n'N': Nie dobieram karty\n")
            if dalszy_krok.lower() == 'g':
                karty_gracza.append(dodaj_karte())
                if wartosc_kart(karty_gracza) > 21:
                    print(f"Przekroczyles 21 przegrywasz! Twoj wynik: {wartosc_kart(karty_gracza)}")

            if wartosc_kart(karty_krupiera) < 15:
                karty_krupiera.append(dodaj_karte())
                if wartosc_kart(karty_krupiera) > 21:
                    print(f"Wygrywasz!! Wartosc kart krupiera przekroczyla 21: {wartosc_kart(karty_krupiera)}")

        print(sprawdz_wynik(karty_g=wartosc_kart(karty_gracza), karty_c=wartosc_kart(karty_krupiera)))


    elif s_menu.lower() == 'q':
        game_is_on = False
