# This class imitates a real pokemon

import random

class Pokemon():
    
    # constructor
    def __init__(self, name, health=50):

        # declare attributes
        self.name = name
        # self.type = type
        self.health = health
        self.damage = 10
        self.speed = random.randint(0, 5)
        self.defended = False

        print(self.name," was created.")

    # declare methods
    def show_state(self):
        print("POKEMON STATE")
        print(self.__dict__)

    def get_damaged(self, enemy_damage):
        if self.defended == False:
            self.health -= enemy_damage
            print(self.name," was damaged ", enemy_damage)
        else:
            print(self.name," defended!")
        self.defended = False

    def attack(self, enemy):
        enemy.get_damaged(self.damage)

    def defend(self):
        self.defended = True
    
    def run(self):
        print(self.name," ran away.")
        