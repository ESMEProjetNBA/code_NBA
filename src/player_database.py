import pandas as pd
import requests
from bs4 import BeautifulSoup

#On règle le problème du / en laissant seulement le nom dans la dataframe
player_data = pd.read_csv("./csv_files/players_data.csv")
player_data['Player'] = player_data['Player'].apply(lambda x : x.split("\\")[0])

#Ici inversement on garde l'autre côté du slash qui va nous servir plus tard (j'appelle l'autre côté ID)...
player_id_data = pd.read_csv("./csv_files/players_data.csv")
player_id_data ['Player'] = player_id_data['Player'].apply(lambda x : x.split("\\")[1])

#L'autre côté du slash (partie droite) on en fait un nouveau dataframe avec une seule colonne contenant seulement la partie droite du /
player_id_only = player_id_data.reindex(columns = ["Player"])
player_id_only.columns = ['ID_Player']


#La je transforme la liste des ID des joueurs en liste
list_of_ID_Player = player_id_only['ID_Player'].tolist()

#Et la je fais une liste qui note toutes les premières lettre de chaque ID
first_letter_of_player = [s[:1] for s in list_of_ID_Player]

#Mais pourquoi faire tout ça ? En fait j'ai remarqué que dans l'url (le lien internet) pour accéder aux pages profiles de chaques joueurs
#c'est toujours le même patern, donc je vais fabriquer les url avec les deux boucles qui suivent

#Ici je mets toutes les URL de chaque profile de joueur dans une liste

def url_profile_player() :
    url_profile_player = []
    for i in range(len(first_letter_of_player)) :
        urlvar1 = "https://www.basketball-reference.com/players/" + first_letter_of_player [i] + "/" + list_of_ID_Player [i] +".html"
        url_profile_player.append(urlvar1)
    return url_profile_player

#Les images de chaques joueurs sont conservés sur le même site avec une url précise donc là j'ai une liste avec toutes les images de joueurs

def url_image_player() :
    url_image_player = []
    for j in range(len(url_profile_player())) :
        urlvar2 = "https://www.basketball-reference.com/req/202106291/images/players/" + list_of_ID_Player[j]  + ".jpg"
        url_image_player.append(urlvar2)
    return url_image_player


df_link_image = pd.DataFrame(url_image_player(), columns = ['Link_image'])
pd.set_option('max_colwidth',40000)

#Maintenant place à la partie scrapping
#Je vais chercher sur la page profile de chaque joueur le poids de chacun et la taille de chacun (ça prend du temps à s'éxecuter)
#Vu le temps que ça prend pour exécuter (environ 7mins) je stocke mon scrapping dans deux fichiers csv différents
#Ce n'est pas problématique car le poids et la taille ne sont pas mises à jours tous les jours
#Dans le cas d'une mise à jour il suffira de re-scrapper une fois le site 

def scrapping_weight(execution) :
    weight_list = []
    if execution == True :
        for weight in range(len(url_profile_player())) :
            get_url = url_profile_player()
            actual_url = get_url[weight]
            req = requests.get(actual_url)
            soup = BeautifulSoup(req.text, 'html.parser')
            weight = soup.find("div", {"id": "meta"})
            weight_span= weight.find_all("span")[2].text
            weight_list.append(weight_span)
        df_weight = pd.DataFrame(weight_list, columns = ['Weight'])   
        return df_weight.to_csv('./csv_files/weight_data_last_backup.csv', index=False)
    else :
        return None 

def scrapping_height(execution) :
    height_list = []
    if execution == True :
        for height in range(len(url_profile_player())) :
            get_url = url_profile_player()
            actual_url = get_url[height]
            req = requests.get(actual_url)
            soup = BeautifulSoup(req.text, 'html.parser')
            height = soup.find("div", {"id": "meta"})
            height_span= height.find_all("span")[1].text
            height_list.append(height_span)
        df_height = pd.DataFrame(height_list, columns = ['Height'])
        return df_height.to_csv('./csv_files/height_data_last_backup.csv', index=False) 
    else :
        return None


#Maintenant je peux afficher ma dataframe au complet avec les valeurs nettoyés (nom, ID_player) et les statistiques, 
#et les valeurs ajoutés via le scrapping (poids, tailles)

df_height_from_csv = pd.read_csv("./csv_files/height_data_last_backup.csv")
df_weight_from_csv = pd.read_csv("./csv_files/weight_data_last_backup.csv")

#On affiche notre dataframe final contenant toutes les données qu'on veut exploiter par la suite
final_player_database = (pd.concat([player_data, player_id_only, df_height_from_csv, df_weight_from_csv, df_link_image], axis = 1)) 


