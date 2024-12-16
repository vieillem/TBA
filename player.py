# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = []

    def get_history(self):
        if not self.history:
            return ""
        msg = "Vous avez déja visité les pièces suivantes:\n"
        for room in self.history:
            msg += f"    - {room.description}\n"
        return msg

    def back(self):
        """
        Permet de revenir à la dernière pièce visitée si possible.
        Retire la dernière pièce de l'historique et y place le joueur.
        Retourne True si le retour a eu lieu, False sinon.
        """
        if not self.history:
            return False
        previous_room = self.history.pop()  # Récupère la dernière pièce visitée
        self.current_room = previous_room
        print(self.current_room.get_long_description())
        return True
    
    # Define the move method.
    def move(self, direction):

        # Vérifier si la sortie est bloquée
        if direction in self.current_room.blocked_exits:
            print(f"\nLa sortie vers le {direction} est bloquée. Vous ne pouvez pas y accéder.\n")
            return False

        old_room = self.current_room

        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits.get(direction)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        self.history.append(old_room)
        history_msg = self.get_history()
        if history_msg.strip():
            print(history_msg)

        return True

    def get_inventory(self):
        if not self.inventory:
            return "Votre inventaire est vide."
        msg = "Vous disposez des items suivants :\n"
        for item in self.inventory:
            msg += f"    - {str(item)}\n"
        return msg