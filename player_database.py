import pandas as pd

player_data = pd.read_csv("players_data.csv")
player_data['Player'] = player_data['Player'].apply(lambda x : x.split("\\")[0])
print(player_data.head())