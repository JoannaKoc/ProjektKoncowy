import random

class Character(object):
    """ Postać gracza. """

    def __init__(self, name = None, race = None, age = 0, gender = None, HP = 0):
        self.name = name
        self.race = race
        self.age = age
        self.gender = gender
        self.HP = HP

    def __str__(self):
        rep = "Twoje imię: " + str(self.name) + "\n" + "Twoja rasa: " + str(self.race) + "\n" + "Twój wiek: " + str(self.age) + "\n" + "Twoja płeć: " + str(self.gender) + "\n" + "Twoje HP: " + str(self.HP) + "\n|"
        return rep

    def tworzenie_postaci(self):
        print("Stworzymy teraz twoją postać, zaczynamy!")
        self.name = input("Wpisz nick postaci: ")
        race = None
        while race != "nord" or race != "breton" or race != "wysoki elf" or race != "khajit":
            race = input("Wpisz rasę postaci: Nord, Breton, Wysoki Elf, Khajit: ").lower()
            if race == "nord" or race == "breton" or race == "wysoki elf" or race == "khajit":
                self.race = race
                break
        self.age = int(input("Podaj wiek postaci: "))
        self.gender = input("Wpisz płeć postaci, k lub m:").lower()
        self.HP = random.randint(0, 20)
        hero = Character(self.name, self.race, self.age, self.gender, self.HP)

    def escape(self):
        print("Uciekasz z pola bitwy.\n")

    def blast(self, enemy):
        print("Wybierasz walkę. \n Twoje strzały dosięgają Twojego przeciwnika.\n")
        enemy.die()

    def hero_die(self):
        print("Umierasz.")

    def heal(self):
        heal_HP = random.randint(0, 8)
        if self.HP >= 10:
            print("Masz max punktów")
        elif self.HP < 10:
            self.HP = self.HP + heal_HP


class Creatures(object):
    """ Obcy w grze strzelance. """

    def __init__(self, HP = 0):
        self.HP = HP

    def __str__(self):
        return "HP przeciwnika: " + str(self.HP)

    def die(self):
        print("Strzały przeciwnika mnie dosięgły - to już mój koniec.")