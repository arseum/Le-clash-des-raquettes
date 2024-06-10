from back.model.joueur import Joueur
from back.model.match import Match


class Tournoi:
    id: int
    nom: str
    lieu: str
    joueurs: [Joueur]
    matchs: [Match]
    date_debut: any
    date_fin: any
    niveau: any
    categorie: any

    def __init__(self):
        pass

    def calcule_format(self):
        nb_participants = len(self.joueurs)
        for i in range(2, 10):
            nb_joueurs_brackets = 2 ** i
            if nb_participants == nb_joueurs_brackets:
                return f"braquet direct de {nb_joueurs_brackets}"
            if nb_participants > nb_joueurs_brackets:
                for j in range(2, i // 2, 2):
                    for k in range(1, 10):
                        if (j + k) * (i // j) == nb_participants:
                            print(f"{j} poule de {i // j}")


def format(nb_participants, nb_table):
    if nb_participants <= 6:
        print("a la ronde")

    nb_joueurs_brackets = 4
    if nb_participants == nb_joueurs_brackets:
        print(f"braquet direct de {nb_joueurs_brackets}")
    if nb_participants > nb_joueurs_brackets:
        for nb_poule in [2, 4]:
            if nb_poule == 2:
                poules = [nb_participants // nb_poule + (j and nb_participants % 2) for j in range(2)]
            else:
                poules = [nb_participants // nb_poule + j for j in
                          [nb_participants / nb_poule % 1 >= 0.25 * k for k in range(1, 5)]]
            temp_tournoi = 14
            for p in poules:
                temp_tournoi += p*(p-1)/2/nb_table * 8
            print(f"{nb_poule} poules: {poules} pour une durée de {temp_tournoi}min")


if __name__ == "__main__":
    for i in range(20):
        print()
        print(f"format de tournoi {4 + i} participants")
        format(4 + i, 2)
