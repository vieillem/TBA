# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.blocked_exits = []
        self.inventory = []
        self.characters = []
        
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        if direction in self.blocked_exits:
            print("\nCe passage est bloqué. Vous ne pouvez pas passer par là !\n")
            return None
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                if exit in self.blocked_exits:
                    exit_string += f"{exit} (bloqué), "
                else:
                    exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        if not self.inventory:
            return "Il n'y a rien ici."
        msg = "On voit:\n"
        for item in self.inventory:
            msg += f"    - {str(item)}\n"
        for npc in self.characters:
            msg += f"    - {str(npc)}\n"
        return msg
