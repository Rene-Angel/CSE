class Character(object):
    def __init__(self, name, health, attack, stats, inventory):
        self.name = name
        self.health = health
        self.stats = stats
        self.inventory = inventory
        self.attack = attack

    def damage(self, target):
        if target.damage(self.attack):
            print("You took Damage.")
            self.health -= self.attack

    def take_damage(self, damage):
        self.health(attack)

    # def interact(item):
    #     item.inventory

# rodin = Character("Rodin", 10000, True, "Immortality",
#                   "'He comes from the heavens above, be as one of the old archangels he wants nothing more than "
#                   "to destroy those who have defied him.' He's tall, dark, and powerful foe. He is "
#                   "nothing more than a weapon's blacksmith with an agenda to run his bar, 'Hell's Gate'. His "
#                   "biggest client is a witch who knows her thing or two about hunting angels and she brings all "
#                   "the goods that Rodin needs, while Rodin himself pours her a drink and starts creating her "
#                   "weapons out of the Halos, Demon Blood, Ebony, and Angelic Tunes from the Heavens. He is "
#                   "very picky when it comes to getting the job done!",
#                   "Angelic Sword, Demon's Eye, Health Vials, Bar Keys")


player = Character("Rodin", 100, 25, None, None)
enemy = Character("Angel", 50, 10, None, None)

(player.attack(enemy))
(enemy.attack(player))
print(self.health)
