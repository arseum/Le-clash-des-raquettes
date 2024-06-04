from back.model.joueur import Joueur
from back.model.tournoi import Tournoi


class Match:
    id: int
    joueur_1: Joueur
    joueur_2: Joueur
    tournoi: Tournoi
    table: int
    score: (int, int)
    heure: any
    phase: any

    def __init__(self):
        pass
