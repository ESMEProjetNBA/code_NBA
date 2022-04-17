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

rating_liste = []
for i in range(len(final_player_database)) :
    rating_part1 = final_player_database["PTS"].iloc[i] + final_player_database["TRB"].iloc[i] + final_player_database["AST"].iloc[i] + final_player_database["STL"].iloc[i] + final_player_database["BLK"].iloc[i]
    rating_part2= final_player_database["FGA"].iloc[i] - final_player_database["FG"].iloc[i] + final_player_database["FTA"].iloc[i] - final_player_database["FT"].iloc[i] + final_player_database["TOV"].iloc[i] 
    rating_part_total = rating_part1 - rating_part2
    rating_liste.append(rating_part_total)

df_rating_liste = pd.DataFrame(rating_liste, columns=["Rating"])
final_player_database_and_rating = pd.concat([final_player_database, df_rating_liste], axis = 1)

""" On va ensuite séparer les joueurs par catégories de taille
Joueur mesurant moins de 1m80 = Cat1
Joueur appartenant à la tranche 1m80 à 1m90 = Cat2
Joueur appartenant à la tranche 1m90 à 2m = Cat3
Joueur appartenant à la tranche 2m à 2,10m = Cat4
Joueur plus grand que 2m10 = Cat5
"""

def Repartition_taille (x):
    if   x <= 180 :
            return "Cat1"
    if  x > 180 and x <= 190 :
            return "Cat2"
    if  x > 190  and x < 200 :
            return "Cat3"
    if  x > 200  and x < 210 :
            return "Cat4"
    if  210 <= x :
            return "Cat5"

final_player_database_and_rating ["Tranche_taille"] = final_player_database_and_rating["Height_cm"].apply(Repartition_taille)

data_first_200 = final_player_database_and_rating.sort_values("Rating", ascending=False).head(312).drop_duplicates(subset='Player', keep='first')
cat_count = data_first_200["Tranche_taille"].value_counts()


#Visualisation de la taille des meilleurs joueurs de NBA par catégories (objectif : savoir qui former chez les jeunes)

objects = ('Cat1(-1m80)', 'Cat2(1m80-1m90)', 'Cat3(1m90-2m)', 'Cat4(2m-2m10)', 'Cat5(+2m10)')
y_pos = np.arange(len(objects))
performance = [cat_count[4],cat_count[3],cat_count[1],cat_count[0],cat_count[2]]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Nombre de joueurs')
plt.title('Nombre de joueurs classés par catégories de taille parmi les 200 meilleurs joueurs de NBA')
plt.show()


#On va créer une dataframe composé uniquement des 5 meilleurs jeunes de moins de 24 ans à leurs postes respectifs
"""
Il existe 5 postes au basket : 
Poste 1 : meneur (Point Guard)
Poste 2 : arrière (Shooting Guard)
Poste 3 : ailier (Small Forward)
Poste 4 : ailier fort (Power Forward)
Poste 5 : pivot (Center)

On va donc chercher les jeunes de moins de 24 ans qui sont les meilleurs à leurs postes respectifs.
Pour objectif de créer la meilleure équipe possible de jeunes ayant un futur prometteur 
"""

Best_young_PG = (data_first_200.loc[(data_first_200['Pos'].str.contains('PG')) & (data_first_200['Age']< 24)].head(1))
Best_young_SG = (data_first_200.loc[(data_first_200['Pos'].str.contains('SG')) & (data_first_200['Age']< 24)].head(1))
Best_young_SF = (data_first_200.loc[(data_first_200['Pos'].str.contains('SF')) & (data_first_200['Age']< 24)].head(1))
Best_young_PF = (data_first_200.loc[(data_first_200['Pos'].str.contains('PF')) & (data_first_200['Age']< 24)].head(1))
Best_young_C = (data_first_200.loc[(data_first_200['Pos'].str.contains('C')) & (data_first_200['Age']< 24)].head(1))

Best_young_team = pd.concat([Best_young_PG,Best_young_SG, Best_young_SF, Best_young_PF, Best_young_C], axis = 0)

print(Best_young_team)
