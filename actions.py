# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command hhhh
# The functions return True if the command was executed successfully, False otherwise. 
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
            
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Toutes les directions valides
        directions= {
            "N": "N", "NORD": "N",
            "S": "S", "SUD": "S",
            "E": "E", "EST": "E",
            "O": "O", "OUEST": "O",
            "U": "U", "UP": "U",
            "D": "D", "DOWN": "D",
            }
        # Get the direction from the list of words.
        direction = list_of_words[1]

        #Convertir la direction en majuscule
        direction = direction.upper()
        if direction in directions:
            direction = directions[direction]
            # Move the player in the direction specified by the parameter.
            player.move(direction)
        else:
            print(f"Direction '{direction}' non reconnue.")
        return True
    
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def history(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des pièces visitées.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Appel à get_history du joueur
        history_msg = game.player.get_history()
        if history_msg.strip():  # Si l'historique n'est pas vide
            print(history_msg)
        else:
            print("\nAucun déplacement effectué pour l'instant.\n")
        return True

    def back(game, list_of_words, number_of_parameters):
        """
        Permet de revenir en arrière dans l'historique des déplacements.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Tente de revenir en arrière
        success = game.player.back()
        if not success:
            print("\nVous ne pouvez pas revenir en arrière, aucun déplacement précédent.\n")
            return False

        # Si retour réussi, afficher la description de la pièce courante (déjà fait dans back()) 
        # et afficher l'historique s'il n'est pas vide.
        history_msg = game.player.get_history()
        if history_msg.strip():
            print(history_msg)
        return True

    def look(game, list_of_words, number_of_parameters):
        """
        Affiche la description de la pièce et la liste des items présents
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        current_room = game.player.current_room
        # Afficher la description de pièce (déjà visible mais on refait pour look)
        print(current_room.get_long_description())
        # Afficher la liste des items dans la pièce
        print(current_room.get_inventory())
        return True

    # NOUVELLE MÉTHODE : take
    def take(game, list_of_words, number_of_parameters):
        """
        Permet de prendre un item présent dans la pièce et de le mettre dans l'inventaire du joueur.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        item_name = list_of_words[1]
        current_room = game.player.current_room
        # Chercher l'item dans la pièce
        item_to_take = None
        for it in current_room.inventory:
            if it.name == item_name:
                item_to_take = it
                break
        
        if item_to_take is None:
            print(f"\nL'objet '{item_name}' n'est pas dans la pièce.\n")
            return False
        
        # Retirer l'item de la pièce et l'ajouter au joueur
        current_room.inventory.remove(item_to_take)
        game.player.inventory.append(item_to_take)
        return True

    # NOUVELLE MÉTHODE : drop
    def drop(game, list_of_words, number_of_parameters):
        """
        Permet de reposer un item de l'inventaire du joueur dans la pièce.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        item_name = list_of_words[1]
        # Chercher l'item dans l'inventaire du joueur
        item_to_drop = None
        for it in game.player.inventory:
            if it.name == item_name:
                item_to_drop = it
                break

        if item_to_drop is None:
            print(f"\nL'objet '{item_name}' n'est pas dans l'inventaire'.\n")
            return False

        # Retirer l'item du joueur et l'ajouter dans la pièce
        game.player.inventory.remove(item_to_drop)
        game.player.current_room.inventory.append(item_to_drop)
        return True

    # NOUVELLE MÉTHODE : check
    def check(game, list_of_words, number_of_parameters):
        """
        Affiche la liste des items dans l'inventaire du joueur.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print(game.player.get_inventory())
        return True