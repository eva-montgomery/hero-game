"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

from hero_game import Character
from hero_game import Hero
from hero_game import Goblin

def main():
    hero = Hero(10,5)
    goblin = Goblin(6,2)
    
    while goblin.is_alive() and hero.is_alive():
        # print("You have %d health and %d power." % (hero.health, hero.power))
        hero.print_status()
        goblin.print_status()
        # print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            goblin.health -= hero.power
            print("You do %d damage to the goblin." % hero.power)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The Goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")

main()
