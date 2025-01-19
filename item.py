"""
Ce fichier item.py définit la classe Item.

Chaque instance d'Item représente un objet dans le jeu
avec un nom, une description et un poids.
"""

# pylint: disable=too-few-public-methods

class Item:
    """
    Classe Item : décrit un objet du jeu, avec nom, description
    et poids, destiné à être ramassé ou déposé par le joueur
    """

    def __init__(self, name, description, weight):
        """
        Initialise l'objet avec :
          - name : le nom de l'objet
          - description : sa description
          - weight : son poids (en kg ou unité arbitraire)
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet,
        sous la forme : "nom : description (weight kg)".
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"
