def calcul_durre_poule(taille_poule, nb_table):
    return taille_poule * (taille_poule - 1) / 2 / nb_table * 8


def determine_poule(nb_participants, nb_poule):
    return [nb_participants // nb_poule + (j and nb_participants % 2) for j in range(2)] if nb_poule == 2 else [
        nb_participants // nb_poule + j for j in [nb_participants / nb_poule % 1 >= 0.25 * k for k in range(1, 5)]]


def format(nb_participants, nb_table, temps_max):
    durre_championat = calcul_durre_poule(nb_participants, nb_table)
    if nb_participants <= 8 and durre_championat <= temps_max:
        print(f"a la ronde pour une durée de {durre_championat}min")

    nb_joueurs_brackets = 4
    if nb_participants <= nb_joueurs_brackets:
        return "au revoir"

    for nb_poule in [2, 4]:
        poules = determine_poule(nb_participants, nb_poule)
        if 2 in poules:
            continue
        temp_tournoi = 14 + sum(calcul_durre_poule(p, nb_table) for p in poules)
        if temp_tournoi <= temps_max:
            print(f"{nb_poule} poules: {poules} pour une durée de {temp_tournoi}min")


if __name__ == "__main__":
    for i in range(20):
        print()
        print(f"format de tournoi {4 + i} participants")
        format(4 + i, 2, 120)
