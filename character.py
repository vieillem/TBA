"""
Ce fichier character.py définit la classe Character,
qui représente un PNJ (Personnage Non Joueur).
Le PNJ peut, selon qu'il soit statique ou non,
se déplacer de façon aléatoire dans les salles adjacentes.
"""

import random
from config import DEBUG


class Character:
    """
    Classe Character : un personnage non joueur avec nom, description,
    salle actuelle, messages à dire, et un paramètre is_static pour
    déterminer s'il bouge ou non.
    """

    def __init__(self, name, description, current_room, msgs, is_static=False):
        """
        Initialise le PNJ avec :
        - name : le nom
        - description : la description
        - current_room : la salle où il se trouve
        - msgs : une liste de messages cycliques
        - is_static : booléen indiquant s'il est immobile
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.is_static = is_static

    def __str__(self):
        """Retourne une représentation textuelle du PNJ."""
        return f"{self.name} : {self.description}"

    def move(self):
        """
        Fait se déplacer le PNJ si is_static est False.
        - 1 chance sur 2 de rester sur place
        - sinon, on choisit une sortie non bloquée au hasard
        Retourne True si le PNJ s'est déplacé, False sinon.
        """
        if self.is_static:
            # On ne log rien dans le DEBUG pour un PNJ statique
            return False

        # 1 chance sur 2 de ne pas bouger
        if random.choice([True, False]) is False:
            if DEBUG:
                print(f"DEBUG: {self.name} ne se déplace pas ce tour-ci.")
            return False

        possible_exits = []
        # Filtre des sorties existantes et non bloquées
        for direction, next_room in self.current_room.exits.items():
            if next_room is not None and direction not in self.current_room.blocked_exits:
                possible_exits.append(next_room)

        if not possible_exits:
            if DEBUG:
                print(f"DEBUG: {self.name} ne peut pas bouger, aucune issue libre.")
            return False

        # Sélection aléatoire d'une salle possible
        new_room = random.choice(possible_exits)
        if self in self.current_room.characters:
            self.current_room.characters.remove(self)
        self.current_room = new_room
        new_room.characters.append(self)

        if DEBUG:
            print(f"DEBUG: {self.name} se déplace vers {new_room.name}")
        return True

    def get_msg(self):
        """
        Affiche un message depuis la liste self.msgs,
        puis réinsère le message à la fin pour un cycle infini.
        """
        if not self.msgs:
            if DEBUG:
                print(f"DEBUG: {self.name} n'a aucun message à dire.")
            return

        msg = self.msgs.pop(0)
        print(msg)
        self.msgs.append(msg)
