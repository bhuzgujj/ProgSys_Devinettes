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
        if checkeur(deviner, nombre_devinable) or essai == 10:
            break
        essai += 1
    pass


def checkeur(string, nb):
    """
    Fonction pour validé le nombre
    :param string: nombre a validé
    :param nb: nombre a comparé
    :return: vrai = nombre valide
    """
    erreur_msg = "ERREUR: Entrez un nombre entier svp"
    try:
        nombre = int(string)
        if isinstance(nombre, int):
            if nombre == nb:
                return True
        else:
            print(erreur_msg)
    except Exception:
        print(erreur_msg)
    return False


if __name__ == '__main__':
    main()
