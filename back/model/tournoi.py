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
