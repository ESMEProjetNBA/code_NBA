import pandas as pd
import requests
from bs4 import BeautifulSoup

player_data = pd.read_csv("players_data.csv")
player_data['Player'] = player_data['Player'].apply(lambda x : x.split("\\")[0])

player_id_data = pd.read_csv("players_data.csv")
player_id_data ['Player'] = player_id_data['Player'].apply(lambda x : x.split("\\")[1])

player_id_only = player_id_data.reindex(columns = ["Player"])
player_id_only.columns = ['ID_Player']
print(pd.concat([player_data, player_id_only], axis = 1)) 


list_of_ID_Player = player_id_only['ID_Player'].tolist()
print(list_of_ID_Player)

first_letter_of_player = [s[:1] for s in list_of_ID_Player]
print(first_letter_of_player)

url_profile_player = []

for i in range(len(first_letter_of_player)) :
    urlvar1 = "https://www.basketball-reference.com/players/" + first_letter_of_player [i] + "/" + list_of_ID_Player [i] +".html"
    url_profile_player.append(urlvar1)

print(url_profile_player)

url_image_player = []

for j in range(len(url_profile_player)) :
    urlvar2 = "https://www.basketball-reference.com/req/202106291/images/players/" + list_of_ID_Player[j]  + ".jpg"
    url_image_player.append(urlvar2)

print(url_image_player)

weight_list = []

for z in range(len(url_profile_player)) :
    actual_url = url_profile_player[z]
    req = requests.get(actual_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    weight = soup.find("span", itemprop="weight")
    weight_list.append(weight.text.strip())

print(weight_list)
