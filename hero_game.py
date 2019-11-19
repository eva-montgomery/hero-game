class Character:
    def __init__(self, character_health, character_power):
        self.health = character_health
        self.power = character_power
        self.name = "body"


    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False 

    def attack(character):
        character.health -= character.power

    def print_status(self):
        print("%s have %d health and %d power." % (self.name, self.health, self.power))  


class Hero(Character):
    pass

#     # def __init__(self, hero_health, hero_power):
#     #     self.health = hero_health
#     #     self.power = hero_power

#     # def attack(self, goblin):
#     #     goblin.health -= self.power

#     # def is_alive(self):
#     #     if self.health > 0:
#     #         return True
#     #     else:
#     #         return False    

    # def print_status(self):
    #     print("You have %d health and %d power." % (self.health, self.power))


class Goblin(Character):
#     # def __init__(self, goblin_health, goblin_power):
#     #     self.health = goblin_health
#     #     self.power = goblin_power 

#     # def attack(self, hero):
#     #     hero.health -= self.power

#     # def is_alive(self):
#     #     if self.health > 0:
#     #         return True
#     #     else:
#     #         return False    

    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))        


# class Zombie(Character):
#         def __init__(self, zombie):
#             if self.health 
      

    


