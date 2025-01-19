"""
Ce fichier player.py définit la classe Player, qui représente le joueur.
Il contient les attributs et méthodes permettant de gérer :
- la pièce actuelle
- l'historique de déplacements
- l'inventaire du joueur
"""

class Player:
    """
    Classe Player : définit l'état et les actions possibles du joueur,
    notamment se déplacer, revenir en arrière, afficher l'historique
    et consulter l'inventaire.
    """

    def __init__(self, name):
        """
        Initialise le joueur avec :
          - name : le nom du joueur
          - current_room : la salle où se trouve le joueur (None au départ)
          - history : la liste des salles précédemment visitées
          - inventory : la liste des objets que le joueur transporte
        """
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = []

    def get_history(self):
        """
        Retourne une chaîne décrivant l'historique des salles visitées.
        Si l'historique est vide, renvoie une chaîne vide.
        """
        if not self.history:
            return ""
        msg = "Vous avez déja visité les pièces suivantes:\n"
        for room in self.history:
            msg += f"    - {room.description}\n"
        return msg

    def back(self):
        """
        Permet de revenir à la dernière salle visitée,
        si l'historique n'est pas vide.
        Renvoie True si le retour a lieu, False sinon.
        """
        if not self.history:
            return False
        previous_room = self.history.pop()
        self.current_room = previous_room
        print(self.current_room.get_long_description())
        return True

    def move(self, direction):
        """
        Déplace le joueur dans la direction indiquée,
        si elle n'est pas bloquée et existe dans la salle courante.
        Renvoie True si le déplacement s'est fait, False sinon.
        """
        if direction in self.current_room.blocked_exits:
            print(f"\nLa sortie vers le {direction} est bloquée. "
                  "Vous ne pouvez pas y accéder.\n")
            return False

        old_room = self.current_room
        next_room = self.current_room.exits.get(direction)

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.current_room = next_room
        print(self.current_room.get_long_description())
        self.history.append(old_room)
        history_msg = self.get_history()
        if history_msg.strip():
            print(history_msg)
        return True

    def get_inventory(self):
        """
        Retourne une description textuelle des objets que transporte le joueur.
        Si l'inventaire est vide, renvoie un message spécifique.
        """
        if not self.inventory:
            return "Votre inventaire est vide."
        msg = "Vous disposez des items suivants :\n"
        for item in self.inventory:
            msg += f"    - {str(item)}\n"
        return msg
