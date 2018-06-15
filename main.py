import random
import pickle
import klasy
import funkcje
import poziom1

def menu():
    print('''\
        ,     \    /      ,        
       / \    )\__/(     / \       
      /   \  (_\  /_)   /   \      
 ____/_____\__\@  @/___/_____\____ 
|             |\../|              |
|              \VV/               |
|      SKYRIM: BIEDA EDITION      |
|_________________________________|
 |    /\ /      \\       \ /\    | 
 |  /   V        ))       V   \  | 
 |/     `       //        '     \| 
 `              V                '
 Menu Główne:
 > 1: Nowa Gra
 > 2: Wczytaj Grę
 > 3: Pomoc
 > wybierasz:
''')

game_state = {
  "hero": None,
  "level": "1",
  "location": "Lecznica"
}
hero = []

print("Na początku gry stworzymy Twoją postać.")
hero = klasy.Character()
hero.tworzenie_postaci()
game_state["hero"] = hero.name, hero.race, hero.age, hero.gender, hero.HP
print(hero)
funkcje.save_game(game_state)
poziom1.poz1lok1()