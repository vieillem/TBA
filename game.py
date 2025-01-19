"""
Ce fichier game.py définit la classe Game, qui gère
la configuration du jeu (pièces, objets, PNJ) et
contient la boucle principale.
"""

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character


class Game:
    """
    Classe principale du jeu.
    Gère la configuration initiale, la boucle de jeu
    ainsi que l'état (fini ou non).
    """

    def __init__(self):
        """Initialise les attributs du jeu."""
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

    def setup(self):
        """
        Configure les commandes, crée les salles, objets et PNJ,
        puis place le joueur dans son point de départ.
        """
        self.commands["help"] = Command("help", " : aide", Actions.help, 0)
        self.commands["quit"] = Command("quit", " : quitter", Actions.quit, 0)
        self.commands["go"] = Command("go", " <dir> : se déplacer (N,E,S,O,U,D)", Actions.go, 1)
        self.commands["history"] = Command("history", " : historique", Actions.history, 0)
        self.commands["back"] = Command("back", " : retour en arrière", Actions.back, 0)
        self.commands["look"] = Command("look", " : observer la pièce", Actions.look, 0)
        self.commands["take"] = Command("take", " <item> : prendre un objet", Actions.take, 1)
        self.commands["drop"] = Command("drop", " <item> : reposer un objet", Actions.drop, 1)
        self.commands["check"] = Command("check", " : vérifier l'inventaire", Actions.check, 0)
        self.commands["talk"] = Command("talk", " <pnj> : parler à un PNJ", Actions.talk, 1)

        village = Room("Village", "dans un village paisible.")
        foret = Room("Forêt", "une forêt dense.")
        porte_chateau = Room("Porte du Chateau", "devant la porte en ruine d'un vieux château.")
        temple = Room("Temple", "dans un temple sacré, empli d'aura mystique.")
        taniere_dragon = Room("Taniere du Dragon", "une tanière sombre où sommeille un dragon.")
        lac_lune = Room("Lac de Lune", "au bord d'un lac scintillant, éclairé par la lune.")
        cimetiere = Room("Cimetière", "un cimetière abandonné, chargé de mystère.")
        tour_guet = Room("Tour de Guet", "au sommet d'une tour donnant vue sur toute la contrée.")

        self.rooms = [village, foret, porte_chateau, temple,
        taniere_dragon, lac_lune, cimetiere, tour_guet]

        village.exits = {"N": foret}
        foret.exits = {"S": village, "O": porte_chateau, "N": cimetiere, "E": lac_lune}
        porte_chateau.exits = {"E": foret, "U": temple, "N": tour_guet}
        taniere_dragon.exits = {"O": cimetiere}
        temple.exits = {"D": porte_chateau}
        lac_lune.exits = {"O": foret}
        cimetiere.exits = {"S": foret, "E": taniere_dragon}
        tour_guet.exits = {"S": porte_chateau}

        # Blocage unique : porte_chateau -> temple
        porte_chateau.blocked_exits.append("U")

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = village

        clef = Item("clef", "une clef rouillée", 1)
        oeufdragon = Item("oeufdragon", "un œuf légendaire de dragon", 3)

        foret.inventory.append(clef)
        taniere_dragon.inventory.append(oeufdragon)

        chevalier = Character(
            "Chevalier",
            "un chevalier en armure, cherchant le Temple",
            porte_chateau,
            ["Je dois accéder au Temple, mais il est bloqué..."],
            is_static=False
        )
        mage = Character(
            "Maitre",
            "un mage ancien, gardien du Temple",
            temple,
            ["Bonjour, le chevalier m'a indiqué d'aller vous parler"],
            is_static=True
        )

        porte_chateau.characters.append(chevalier)
        temple.characters.append(mage)

    def play(self):
        """
        Boucle principale du jeu : on exécute setup,
        on affiche un message de bienvenue, puis on
        traite les commandes tant que le jeu n'est pas fini.
        """
        self.setup()
        self.print_welcome()
        while not self.finished:
            cmd_ok = self.process_command(input("> "))
            if cmd_ok:
                self.move_npcs()

    def move_npcs(self):
        """Fait se déplacer les PNJ non statiques."""
        for room in self.rooms:
            for npc in list(room.characters):
                npc.move()

    def process_command(self, command_string) -> bool:
        """Analyse la commande saisie et l'exécute si elle est reconnue."""
        if not command_string.strip():
            return False

        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour la liste.\n")
            return False

        command = self.commands[command_word]
        success = command.action(self, list_of_words, command.number_of_parameters)
        return success

    def print_welcome(self):
        """Affiche un message de bienvenue et la description de la pièce de départ."""
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Votre objectif : déposer l'oeuf de dragon au Village.")
        print("Commencez par parler au Chevalier ('talk chevalier') pour en savoir plus.")
        print(self.player.current_room.get_long_description())

    def unlock_temple(self):
        """Débloque l'accès Temple depuis PorteChateau quand la clef est prise."""
        for room in self.rooms:
            if room.name == "Porte du Chateau":
                if "U" in room.blocked_exits:
                    room.blocked_exits.remove("U")
                    print("\nUn mécanisme se déverrouille : l'accès au Temple est ouvert !\n")

    def check_drop(self, item_name):
        """Vérifie si on dépose l'oeuf de dragon dans le village => fin du jeu."""
        if item_name == "oeufdragon":
            if self.player.current_room.name == "Village":
                print("\nVous déposez l'oeuf au Village. Bravo, quête accomplie !")
                self.finished = True

    def check_victory(self):
        """
        Appelée après certaines actions pour vérifier
        si le joueur a gagné (ici géré par check_drop).
        """
        return

def main():
    """Fonction principale : crée un objet Game puis lance la boucle de jeu."""
    Game().play()

if __name__ == "__main__":
    main()
