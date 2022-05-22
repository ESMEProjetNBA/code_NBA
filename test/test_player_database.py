from src.player_database import scrapping_height
from src.player_database import scrapping_weight

#Exemple de Test Unitaire
def test_scrapping_height():
    scrapping_w = scrapping_height(False) 
    expected_scrapping_w = None
    assert scrapping_w == expected_scrapping_w

def test_scrapping_weight():
    scrapping_h = scrapping_weight(False) 
    expected_scrapping_h = None
    assert scrapping_h == expected_scrapping_h

