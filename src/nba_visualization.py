import pandas as pd
import numpy as np
from player_database import final_player_database
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()


"""
On va évaluer le niveau de chaque joueur en faisant le calcul officiel proposé par la NBA
Un moyen d’évaler de la performance individuelle est la notion d’évaluation 
(ou « rating » en anglais). Son calcul est relativement simple :
(Points + Rebonds + Passes + Interceptions + Contres) – [(Tirs tentés – Tirs réussis) + (Lancers tentés – Lancers réussis) + Pertes de balle)]
Dans notre cas : (PTS + TRB + AST + STL + BLK) - [(FGA - FG) + (FTA - FT) + TOV]
"""

def rating_liste () :
        rating_liste = []
        for i in range(len(final_player_database)) :
                rating_part1 = final_player_database["PTS"].iloc[i] + final_player_database["TRB"].iloc[i] + final_player_database["AST"].iloc[i] + final_player_database["STL"].iloc[i] + final_player_database["BLK"].iloc[i]
                rating_part2= final_player_database["FGA"].iloc[i] - final_player_database["FG"].iloc[i] + final_player_database["FTA"].iloc[i] - final_player_database["FT"].iloc[i] + final_player_database["TOV"].iloc[i] 
                rating_part_total = rating_part1 - rating_part2
                rating_liste.append(rating_part_total)
        return rating_liste

df_rating_liste = pd.DataFrame(rating_liste(), columns=["Rating"])
final_player_database_and_rating = pd.concat([final_player_database, df_rating_liste], axis = 1)
data_first_200 = final_player_database_and_rating.sort_values("Rating", ascending=False).head(312).drop_duplicates(subset='Player', keep='first')



#On va créer une dataframe composé uniquement des 5 meilleurs jeunes de moins de 24 ans à leurs postes respectifs
"""
Il existe 5 postes au basket : 
Poste 1 : meneur (Point Guard)
Poste 2 : arrière (Shooting Guard)
Poste 3 : ailier (Small Forward)
Poste 4 : ailier fort (Power Forward)
Poste 5 : pivot (Center)
On va donc chercher les jeunes de moins de x ans qui sont les meilleurs à leurs postes respectifs.
Pour objectif de créer la meilleure équipe possible de jeunes ayant un futur prometteur 
"""
def Best_young_team(x):
        Best_young_PG = (data_first_200.loc[(data_first_200['Pos'].str.contains('PG')) & (data_first_200['Age']< x)].head(1))
        Best_young_SG = (data_first_200.loc[(data_first_200['Pos'].str.contains('SG')) & (data_first_200['Age']< x)].head(1))
        Best_young_SF = (data_first_200.loc[(data_first_200['Pos'].str.contains('SF')) & (data_first_200['Age']< x)].head(1))
        Best_young_PF = (data_first_200.loc[(data_first_200['Pos'].str.contains('PF')) & (data_first_200['Age']< x)].head(1))
        Best_young_C = (data_first_200.loc[(data_first_200['Pos'].str.contains('C')) & (data_first_200['Age']< x)].head(1))
        Best_young_team= pd.concat([Best_young_PG,Best_young_SG, Best_young_SF, Best_young_PF, Best_young_C], axis = 0)
        Best_young_team.drop(Best_young_team.iloc[:, 5:31], axis = 1, inplace = True)
        return Best_young_team





