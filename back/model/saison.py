from back.model.tournoi import Tournoi


class Saison:
    id: int
    tournois: [Tournoi]
    date_debut: any
    date_fin: any

    def __init__(self):
        pass
