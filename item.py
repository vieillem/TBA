class Item:
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        # Retourne une représentation textuelle de l’item
        return f"{self.name} : {self.description} ({self.weight} kg)"