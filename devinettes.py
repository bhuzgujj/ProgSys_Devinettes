#!/usr/bin/env python3
"""
Jeu de devinettes

Auteur: Émile Boucher
"""

import random

MINIMUM = 1
MAXIMUM = 100


def main():
    """
    Code princiapale du jeu de devinette
    """
    print("Bonjour, je m'appelle Emilex 2020")
    nombre_devinable = random.randrange(MINIMUM, MAXIMUM + 1)
    print(f"J'ai choisi un nombre entier entre {MINIMUM} et {MAXIMUM}")
    print("Pouvez-vous le deviner ?")
    while True:
        loop_principale(nombre_devinable)
        print('Voulez-vous rejouer?')
        reponse = input().upper()
        if reponse == 'NON' or reponse == 'N':
            break
    pass


def loop_principale(nombre_devinable):
    """
    La fonction de jeu principale
    :param nombre_devinable: Le nombre a deviner
    :return: retour a la fonction
    """
    essai = 1
    nombre_essayer = []
    while True:
        deviner = input()
        print(f"Essai {essai}: {deviner}")
        sortie = cheat_code(deviner, essai, nombre_essayer)
        if not sortie and validateur_format(deviner):
            nombre_essayer.append(deviner)
            essai += 1
            if int(deviner) > int(nombre_devinable):
                print('PLUS PETIT')
            elif int(deviner) < int(nombre_devinable):
                print('PLUS GRAND')
            else:
                print('BRAVO')
                sortie = True
        if sortie:
            break
    return


def cheat_code(code_entrer, nb_essais, nb_essayer):
    """
    Fonction qui détecte et gère les "Cheat code"
    :param nb_essayer: Les nombres essayer
    :param nb_essais: Nombre d'essais fait
    :param code_entrer: Code entrer
    :return: L'id du "Cheat code" (0 pour aucun)
    """
    if code_entrer == 'ABC':
        return True
    return False


def validateur_format(string):
    """
    Fonction pour validé le nombre
    :param string: nombre a validé
    :return: vrai = nombre valide
    """
    erreur_msg = "ERREUR: Entrez un nombre entier svp"
    try:
        nombre = int(string)
        if isinstance(nombre, int):
            return True
    except ValueError:
        print(erreur_msg)
    return False


if __name__ == '__main__':
    main()
