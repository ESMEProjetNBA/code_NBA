import player_database

print(player_database)

"""
Il existe 5 postes au basket : 
Poste 1 : meneur (point guard)
Poste 2 : arrière (shooting guard)
Poste 3 : ailier (small forward)
Poste 4 : ailier fort (power forward)
Poste 5 : pivot (center)

L’évaluation
Un autre moyen d’évaluation de la performance individuelle mis en avant par la NBA est la notion d’évaluation 
(ou « rating » en anglais). Son calcul est relativement simple :
(Points + Rebonds + Passes + Interceptions + Contres) – [(Tirs tentés – Tirs réussis) + (Lancers tentés – Lancers réussis) + Pertes de balle)]
Dans notre cas : (PTS + TRB + AST + STL + BLK) - [(FGA - FG) + (FTA - FT) + TOV]
"""