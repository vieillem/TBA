"""
Ce fichier command.py définit la classe Command.

Chaque instance de Command représente une commande du jeu,
avec un mot-clé, un texte d'aide, une fonction à exécuter
et un nombre de paramètres attendu.
"""
# pylint: disable=too-few-public-methods

class Command:
    """
    Classe Command : décrit une commande du jeu avec son
    mot-clé, sa description d'aide, la fonction associée
    et le nombre de paramètres requis.
    """

    def __init__(self, command_word, help_string, action, number_of_parameters):
        """
        Initialise la commande avec :
          - command_word : le mot-clé (ex: 'go', 'help')
          - help_string : le texte d'aide affiché
          - action : la fonction à exécuter pour cette commande
          - number_of_parameters : le nombre de paramètres requis
        """
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    def __str__(self):
        """
        Retourne le mot-clé suivi de la chaîne d'aide,
        pour représenter la commande sous forme de texte.
        """
        return self.command_word + self.help_string
