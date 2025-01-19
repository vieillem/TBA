"""
Ce fichier actions.py définit la classe Actions, qui regroupe des méthodes statiques
pour traiter diverses commandes (go, quit, help, history, etc.).
Chaque fonction prend en paramètre :
 - game : l'objet principal du jeu
 - list_of_words : la liste des mots composant la commande
 - number_of_parameters : le nombre de paramètres requis par la commande

Chaque fonction renvoie True si la commande aboutit, False sinon.
"""


from config import DEBUG

# MSG0 : message d'erreur si la commande ne prend pas de paramètre.
# MSG1 : message d'erreur si la commande prend un paramètre unique.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"


class Actions:
    """
    Classe statique : contient les méthodes associées aux commandes du jeu.
    """

    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """Commande pour se déplacer dans une direction donnée."""
        player = game.player
        length_cmd = len(list_of_words)
        if length_cmd != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        directions = {
            "N": "N", "NORD": "N",
            "S": "S", "SUD": "S",
            "E": "E", "EST": "E",
            "O": "O", "OUEST": "O",
            "U": "U", "UP": "U",
            "D": "D", "DOWN": "D"
        }

        direction = list_of_words[1].upper()
        if direction in directions:
            direction = directions[direction]
            success = player.move(direction)
            if success:
                game.check_victory()
            return success

        print(f"Direction '{direction}' non reconnue.")
        return False

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """Commande pour quitter la partie (game.finished = True)."""
        length_cmd = len(list_of_words)
        if length_cmd != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """Commande pour afficher la liste des commandes disponibles."""
        length_cmd = len(list_of_words)
        if length_cmd != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """Commande pour afficher l'historique des déplacements du joueur"""
        length_cmd = len(list_of_words)
        if length_cmd != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        history_msg = game.player.get_history()
        if history_msg.strip():
            print(history_msg)
        else:
            print("\nAucun déplacement effectué pour l'instant.\n")
        return True

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """Commande pour revenir à la salle précédente."""
        length_cmd = len(list_of_words)
        if length_cmd != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        success = game.player.back()
        if not success:
            print("\nVous ne pouvez pas revenir en arrière, aucun déplacement précédent.\n")
            return False

        history_msg = game.player.get_history()
        if history_msg.strip():
            print(history_msg)
        return True

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """Commande pour observer la salle courante (description, inventaire)."""
        length_cmd = len(list_of_words)
        if length_cmd != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        current_room = game.player.current_room
        print(current_room.get_long_description())
        print(current_room.get_inventory())
        return True

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """Commande pour prendre un objet dans la salle et l'ajouter à l'inventaire."""
        length_cmd = len(list_of_words)
        if length_cmd != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        item_name = list_of_words[1]
        current_room = game.player.current_room
        item_to_take = None
        for it in current_room.inventory:
            if it.name.lower() == item_name.lower():
                item_to_take = it
                break

        if item_to_take is None:
            print(f"\nL'objet '{item_name}' n'est pas dans la pièce.\n")
            return False

        current_room.inventory.remove(item_to_take)
        game.player.inventory.append(item_to_take)

        if item_to_take.name.lower() == "clef":
            game.unlock_temple()
        return True

    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """Commande pour déposer un objet de l'inventaire dans la salle courante."""
        length_cmd = len(list_of_words)
        if length_cmd != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        item_name = list_of_words[1]
        item_to_drop = None
        for it in game.player.inventory:
            if it.name.lower() == item_name.lower():
                item_to_drop = it
                break

        if item_to_drop is None:
            print(f"\nL'objet '{item_name}' n'est pas dans l'inventaire'.\n")
            return False

        game.player.inventory.remove(item_to_drop)
        game.player.current_room.inventory.append(item_to_drop)
        game.check_drop(item_name.lower())
        return True

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """Commande pour afficher l'inventaire du joueur."""
        length_cmd = len(list_of_words)
        if length_cmd != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print(game.player.get_inventory())
        return True

    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """Commande pour parler à un PNJ présent dans la salle."""
        length_cmd = len(list_of_words)
        if length_cmd != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        npc_name = list_of_words[1]
        current_room = game.player.current_room

        npc_found = None
        for npc in current_room.characters:
            if npc.name.lower() == npc_name.lower():
                npc_found = npc
                break

        if not npc_found:
            print(f"\nIl n'y a pas de personnage nommé '{npc_name}' ici.\n")
            return False

        if DEBUG:
            print(f"DEBUG: PNJ trouvé, exécution de get_msg() pour {npc_found.name}")
        npc_found.get_msg()

        if npc_found.name.lower() == "chevalier":
            print("\nLe Chevalier : Trouve la clef dans la Forêt afin de débloquer "
             "la route vers le Temple et parler au Maitre.\n")
        elif npc_found.name.lower() == "maitre":
            print("\nLe Maître : Rapportes l'oeuf de dragon (qui se situe dans la Tanière du) "
             "dragon au Village pour réussir.\n")

        return True
