import os

def show_board(grille, ligne_actuelle=None, colonne_actuelle=None):
    os.system("cls")
    print("\n" + "="*21)
    for idx, ligne in enumerate(grille):
        ligne_str = ""
        for i, valeur in enumerate(ligne):
            if idx == ligne_actuelle and i == colonne_actuelle:
                if valeur == 0:
                    ligne_str += "[_] "
                else:
                    ligne_str += f"[{valeur}] "
            else:
                # Affichage normal
                if valeur == 0:
                    ligne_str += "_ "
                else:
                    ligne_str += f"{valeur} "
            
            # Séparateurs verticaux
            if i == 2 or i == 5:
                ligne_str += "| "
        
        print(ligne_str.rstrip())
        
        # Séparateurs horizontaux
        if idx == 2 or idx == 5:
            print("------+-------+------")
    print("="*21)
