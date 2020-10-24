#!/usr/bin/env python3
"""
Jeu de devinettes

Auteur: Émile Boucher
"""

import random

# Constante
MINIMUM = 1
MAXIMUM = 100
NOMBRE_ESSAI_MAX = 10


def main():
    """
    Code princiapale du jeu de devinette
    """
    print("Bonjour, je m'appelle Emilex 2020")
    nombre_devinable = random.randrange(MINIMUM, MAXIMUM + 1)
    print(f"J'ai choisi un nombre entier entre {MINIMUM} et {MAXIMUM}")
    print('Pouvez-vous le deviner ?')
    reponse = 'OUI'
    nombre_partie = 0
    nombre_essais = 0
    while True:
        if reponse == 'OUI' or reponse == 'O':
            print('')
            nombre_essais += loop_principale(nombre_devinable)
            nombre_partie += 1
            print('Voulez-vous rejouer [O/N]?')
        else:
            print('Veuillez entrer OUI ou NON. ("O" ou "N")')
        reponse = input().upper()
        if reponse == 'NON' or reponse == 'N':
            print(f'Nombre de parties jouées: {nombre_partie}')
            print(f"Nombre d'essais: {nombre_essais}")
            print(f"Moyenne d'essais par partie: {nombre_essais / nombre_partie}")
            print('Au revoir!')
            break
    pass


def loop_principale(nombre_devinable):
    """
    La fonction de jeu principale
    :param nombre_devinable: Le nombre a deviner
    """
    essai = 1
    nombre_essayer = []
    while True:
        print(f'Essai {essai}: ', end=' ')
        deviner = input()
        sortie = cheat_code(deviner, essai, nombre_essayer, nombre_devinable)
        if not sortie and validateur_format(deviner):
            nombre_essayer.append(int(deviner))
            essai += 1
            if int(deviner) > int(nombre_devinable):
                print('Votre nombre est trop grand...')
            elif int(deviner) < int(nombre_devinable):
                print('Votre nombre est trop petit...')
            else:
                print('Bravo, vous avez deviné le nombre')
                print(f'Votre séquense gagnante est: {nombre_essayer}')
                sortie = True
        if sortie:
            break
        if essai > 10:
            print(f'Désolé, vous avez échoué après {NOMBRE_ESSAI_MAX} tentatives')
            print(f'Le nombre choisi était {nombre_devinable}')
            break
    return essai


def cheat_code(code_entrer, nb_essais, nb_essayer, devinable):
    """
    Fonction qui détecte et gère les "Cheat code"
    :param devinable: Le nombre a deviné
    :param nb_essayer: Les nombres essayer
    :param nb_essais: Nombre d'essais fait
    :param code_entrer: Code entrer
    :return: L'id du "Cheat code" (0 pour aucun)
    """
    if code_entrer == 'PPP':
        print(f'Désolé, vous avez échoué après {nb_essais} tentatives')
        print(f'Le nombre choisi était {devinable}')
        return True
    elif code_entrer == 'GGG':
        nb_essayer.append(code_entrer)
        print('Bravo, vous avez deviné le nombre')
        print(f'Votre séquense gagnante est: {nb_essayer}')
        return True
    return False


def validateur_format(string):
    """
    Fonction pour validé le nombre
    :param string: nombre a validé
    :return: vrai = nombre valide
    """
    erreur_msg = 'ERREUR: Entrez un nombre entier svp'
    try:
        nombre = int(string)
        if isinstance(nombre, int):
            return True
    except ValueError:
        print(erreur_msg)
    return False


if __name__ == '__main__':
    main()
