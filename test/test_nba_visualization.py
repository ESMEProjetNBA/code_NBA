from src.nba_visualization import Repartition_taille

#Exemple de Test Unitaire
def test_repartition():
    taille = Repartition_taille(195)
    expected_repartition = "Cat3"
    assert taille == expected_repartition

