# this class imitates a pokemon item

class Item():
    
    # constructor
    def __init__(self, type_id):
        
        types = ["Potion", "Boost"]

        self.type = types[type_id] # Potion, Boost
        self.potency = 10

    # methods
    def show_state(self):
        print(self.__dict__)

    def use(self, receiver):
        
        if self.type == "Potion":
            # do something for potion
            # receiver.health += self.potency
            pass
        elif self.type == "Boost":
            # do something
            # receiver.attack
            pass