# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        history_cmd = Command("history", " : afficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = history_cmd
        back_cmd = Command("back", " : revenir en arrière", Actions.back, 0)
        self.commands["back"] = back_cmd
        
        # Setup rooms

        forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(tower)
        cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(cave)
        cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(cottage)
        swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(swamp)
        castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(castle)
        crystal_cavern = Room("Crystal Cavern", "dans une caverne scintillante où des cristaux magiques illuminent les ténèbres.")
        sky_garden = Room("Sky Garden", "dans un jardin suspendu flottant entre les nuages.")
        dragon_lair = Room("Dragon Lair", "dans l'antre d'un dragon, avec des montagnes d'or et de joyaux.")
        shadow_forest = Room("Shadow Forest", "dans une forêt où les ombres semblent s'animer.")
        silver_lake = Room("Silver Lake", "au bord d'un lac argenté qui réfléchit un ciel étoilé.")
        ancient_library = Room("Ancient Library", "dans une bibliothèque ancienne remplie de livres magiques.")
        obsidian_tower = Room("Obsidian Tower", "dans une tour noire faite d'obsidienne, avec des gravures étranges.")
        mystic_cavern = Room("Mystic Cavern", "dans une grotte où des runes brillent sur les murs.")
        enchanted_meadow = Room("Enchanted Meadow", "dans une prairie enchantée où des lucioles dansent dans la lumière.")
        golden_temple = Room("Golden Temple", "dans un temple étincelant, baigné de lumière dorée.")
        whispering_cliffs = Room("Whispering Cliffs", "au sommet de falaises où des voix murmurent dans le vent.")
        frozen_sanctuary = Room("Frozen Sanctuary", "dans un sanctuaire glacé, avec des sculptures de glace.")
        fiery_depths = Room("Fiery Depths", "dans les profondeurs embrasées d'une montagne volcanique.")
        celestial_palace = Room("Celestial Palace", "dans un palais céleste avec des colonnes dorées et un plafond étoilé.")
        abyssal_chasm = Room("Abyssal Chasm", "au bord d'un gouffre abyssal qui semble sans fin.")
        floating_island = Room("Floating Island", "sur une île flottante entourée de cascades aériennes.")

        self.rooms = [forest, tower, cave, cottage, swamp, castle, crystal_cavern, sky_garden, dragon_lair, shadow_forest, silver_lake, ancient_library, obsidian_tower, mystic_cavern, enchanted_meadow, golden_temple, whispering_cliffs, frozen_sanctuary, fiery_depths, celestial_palace, abyssal_chasm, floating_island]


        # Create exits for rooms

        forest.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None, "U" : None, "D" : None}
        forest.blocked_exits.append("E")  # Bloquer le retour vers la tour
        tower.exits = {"N" : cottage, "E" : None, "S" : swamp, "O" : forest, "U" : obsidian_tower, "D" : None}
        cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None, "U" : None, "D" : crystal_cavern}
        cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave, "U" : ancient_library, "D" : None}
        swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle, "U" : None, "D" : fiery_depths}
        castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None, "U" : golden_temple, "D" : None}
        crystal_cavern.exits = {"N" : None, "E" : None, "S" : None, "O" : None,"U": cave, "D" : None}
        obsidian_tower.exits = {"D": tower, "N": shadow_forest, "E" : None, "S" : None, "O" : None,"U": None}
        ancient_library.exits = {"D": cottage, "N" : None, "E" : None, "S" : None, "O" : None,"U": None}
        fiery_depths.exits = {"U": swamp, "D": None, "N" : None, "E" : None, "S" : None, "O" : None}
        golden_temple.exits = {"D": castle, "N": celestial_palace, "E" : None, "S" : None, "O" : None,"U": None}
        celestial_palace.exits = {"S": golden_temple, "E": floating_island, "O" : None,"U": None, "D": None, "N": None}
        floating_island.exits = {"O": celestial_palace, "N": sky_garden, "D" : None, "U" : None, "E" : None, "S" : None}
        sky_garden.exits = {"S": floating_island, "U": enchanted_meadow, "D": None, "N" : None, "E" : None, "O" : None}
        enchanted_meadow.exits = {"D": sky_garden, "E": whispering_cliffs, "O": None, "N" : None, "U" : None, "S" : None}
        whispering_cliffs.exits = {"O": enchanted_meadow, "D": None, "N" : None, "E" : None, "S" : None, "U" : None}
        shadow_forest.exits = {"S": obsidian_tower, "E": silver_lake, "D": None, "N" : None, "U" : None, "O" : None}
        silver_lake.exits = {"O": shadow_forest, "N": dragon_lair, "D": None, "U" : None, "E" : None, "S" : None}
        dragon_lair.exits = {"S": silver_lake, "D": None, "N" : None, "E" : None, "O" : None, "U": None}
        frozen_sanctuary.exits = {"D": abyssal_chasm, "O": None, "N" : None, "E" : None, "S" : None, "U": None}
        abyssal_chasm.exits = {"U": frozen_sanctuary, "D": None, "N" : None, "E" : None, "S" : None, "O": None}

        # Ajouter des passages bloqués
        
        swamp.blocked_exits.append("N")  # Nord bloqué depuis le marécage
        tower.blocked_exits.append("S")  # Sud bloqué depuis la tour


        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp


    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Ignore empty commands
        if not command_string.strip():
            return  # Ne rien faire si la commande est vide

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
