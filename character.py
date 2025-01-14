# character.py
# NOUVEAU FICHIER

import random  
from config import DEBUG  
from room import Room   

class Character:
    """
    Représente un personnage non joueur (PNJ).
    """

    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs  # liste des messages que le PNJ peut dire (en boucle)

    def __str__(self):
        """
        Retourne une représentation textuelle du PNJ.
        """
        return f"{self.name} : {self.description}"

    def move(self):
        """
        A chaque tour de jeu, le PNJ a une chance sur deux de se déplacer.
        S'il se déplace, il va dans une pièce adjacente (exits) au hasard.
        Retourne True s'il s'est déplacé, False sinon.
        """

        if random.choice([True, False]) is False:
            if DEBUG:
                print(f"DEBUG: {self.name} ne se déplace pas.")
            return False

        # Récupérer les salles adjacentes dans self.current_room.exits
        possible_exits = []
        for direction, room in self.current_room.exits.items():
            if room is not None: 
                possible_exits.append(room)

        if not possible_exits:
            if DEBUG:
                print(f"DEBUG: {self.name} est bloqué, aucune sortie disponible.")
            return False

        # Choisir une pièce aléatoire
        new_room = random.choice(possible_exits)

        # Retirer le PNJ de l'ancienne salle
        if self in self.current_room.characters:
            self.current_room.characters.remove(self)

        # Placer le PNJ dans la nouvelle salle
        self.current_room = new_room
        new_room.characters.append(self)

        if DEBUG:
            print(f"DEBUG: {self.name} se déplace vers {new_room.name}")

        return True

    def get_msg(self):
        """
        Affiche cycliquement les messages associés au PNJ.
        On supprime le premier message de la liste et on l'affiche,
        puis on le remet à la fin pour un cycle infini.
        """
        if not self.msgs:
            # PNJ sans message
            if DEBUG:
                print(f"DEBUG: {self.name} n'a pas de message à dire.")
            return

        # Récupérer le premier message
        msg = self.msgs.pop(0)
        print(msg)
        # Le remettre à la fin de la liste
        self.msgs.append(msg)