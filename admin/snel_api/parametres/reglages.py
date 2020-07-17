"""
    Ce module contient tous les parametres de fonctionnement des compteurs, des transfos et autres
"""

# Prix d'un wattheure d'energie electrique en francs congolais
PRIX_PAR_WATT = 100

# Le niveau en pourcentage à partir du quel on va considerer le transformateur en surcharge (Warning)
MIN_TRANSFO_ALERT_LEVEL = 75

# Classes des compteurs
# A : classe domestique
# B : classe semi-industrielle
# C : classe industrielle
COMPTEURS_CLASSES = {'A': 10000, 'B': 50000, 'C': 100000}