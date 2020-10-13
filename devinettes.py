#!/usr/bin/env python3
"""
Jeu de devinettes

Auteur: Émile Boucher
"""

import random


def main():
    """
    Code princiapale du jeu de devinette
    """
    print("Bonjour, je m'appelle Emilex 2020")
    minimum = 1
    maximum = 100
    essai = 1
    nombre_devinable = random.randrange(minimum, maximum + 1)
    print(f"J'ai choisi un nombre entier entre {minimum} et {maximum}")
    print("Pouvez-vous le deviner ?")
    while True:
        deviner = 0
        print(f"Essai {essai}: {deviner}")
        essai += 1
        if deviner == nombre_devinable: break
    pass


def checkeur(str):
    erreur_msg = "ERREUR: Entrez un nombre entier svp"
    try:
        nombre = int(str)
        if type(nombre) is type(1nt):
            return
        else:
            print(erreur_msg)
    except Exception:
        print(erreur_msg)


if __name__ == '__main__':
    main()
