from xmlrpc.client import boolean
from player_database import scrapping_weight
from player_database import scrapping_height
from nba_visualization import Best_young_team
import pandas as pd
from flask import Flask, render_template


app = Flask(__name__)


scrapping_weight(False)
scrapping_height(False)

age_junior = int(input('Entrez âge max des joueurs de l\'équipe : '))
data = Best_young_team(age_junior)
data.to_csv('./csv_files/Best_young_team.csv', index=False)

@app.route("/tables")
def show_tables():
    data_final = pd.read_csv('./csv_files/Best_young_team.csv')
    data_final.set_index(['Player'], inplace=True)
    data_final.index.name=None
    return render_template('view.html', tables=[data_final.to_html(classes='data')], titles=data_final.columns.values)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False)

