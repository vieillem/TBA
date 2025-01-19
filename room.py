"""
Ce fichier room.py définit la classe Room.

La classe Room décrit un lieu du jeu, avec :
- un nom et une description
- un dictionnaire de sorties (exits)
- une liste de sorties bloquées (blocked_exits)
- un inventaire (inventory)
- une liste de PNJ présents (characters)
"""

class Room:
    """
    Classe Room : représente un lieu du jeu,
    avec sorties, inventaire et éventuels PNJ.
    """

    def __init__(self, name, description):
        """
        Initialise la salle avec :
          - name : le nom du lieu
          - description : la description textuelle
          - exits : un dictionnaire {direction: autre_room}
          - blocked_exits : liste de directions bloquées
          - inventory : liste d'objets présents
          - characters : liste de PNJ présents
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.blocked_exits = []
        self.inventory = []
        self.characters = []

    def get_exit(self, direction):
        """
        Retourne la Room associée à la direction donnée,
        s'il y en a une et si elle n'est pas bloquée.
        Affiche un message si la direction est bloquée.
        Renvoie None si la direction est invalide ou bloquée.
        """
        if direction in self.exits:
            return self.exits[direction]
        if direction in self.blocked_exits:
            print("\nCe passage est bloqué. Vous ne pouvez pas passer par là !\n")
            return None
        return None

    def get_exit_string(self):
        """
        Construit et renvoie une chaîne décrivant les sorties disponibles.
        Indique également celles qui sont bloquées.
        """
        exit_string = "Sorties: "
        for direction_key in self.exits:
            if self.exits[direction_key] is not None:
                if direction_key in self.blocked_exits:
                    exit_string += f"{direction_key} (bloqué), "
                else:
                    exit_string += direction_key + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_long_description(self):
        """
        Retourne une description longue de la salle,
        incluant la description textuelle et la liste des sorties.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """
        Renvoie une chaîne décrivant le contenu de la salle :
        items et PNJ présents. Si rien n'est présent, renvoie un message adapté.
        """
        if not self.inventory and not self.characters:
            return "Il n'y a rien ici."
        msg = "On voit:\n"
        for item_obj in self.inventory:
            msg += f"    - {str(item_obj)}\n"
        for npc in self.characters:
            msg += f"    - {str(npc)}\n"
        return msg
