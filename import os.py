import os
import random as rand

hasla=[
    "AUDI",
    "BMW",
    "MERCEDES",
    "RENAULT",
    "HONDA",
    "NISSAN",
    "FORD",
    "HYUNDAI",
    "VOLKSWAGEN",
    "TOYOTA"
]


SZUBIENICA = ['''






''','''






=========''','''

      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




def wisielec(bledy):
    os.system("cls")
    print(SZUBIENICA[bledy])
    print("Zgadnij literę: ")

# def gra(wylosowane_haslo):
#     dlugosc = wylosowane_haslo.__len__()
#     bledy = 0

def generuj_haslo():
    wylosowane_haslo = rand.choice(hasla)
    return wylosowane_haslo


def main():
    wylosowane_haslo = generuj_haslo()
    dlugosc = wylosowane_haslo.__len__()
    bledy = 0
    while bledy < 10:
        wisielec(bledy)
        litera = input()
        if litera in wylosowane_haslo:
            print("Zgadłeś")
        else:
            bledy += 1
            print("Nie zgadłeś")
    print("Koniec gry")



gra(rand.choice(hasla))


#hangman in console
# import os.py
import os
import random as rand
