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

    


def wisielec(szanse):
    os.system("cls")
    print(SZUBIENICA[szanse])
            
def gra(wylosowane_haslo):
    
    dlugosc = wylosowane_haslo.__len__() 
    wisielec(0)



gra(rand.choice(hasla))
