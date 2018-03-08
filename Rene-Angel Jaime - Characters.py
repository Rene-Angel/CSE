class Character(object):
    def __init__(self, name, health, attack, status_effects, information, inventory):
        self.name = name
        self.health = health
        self.status_effects = status_effects
        self.information = information
        self.inventory = inventory
        self.attack_amt = attack
        self.talk = "Hello."

    def attack(self, target):
        if target.damage(self.attack_amt):

    def take_damage(self, amt):

    def interact(self):
        item.inventory

    def take_damage(self):


rodin = Character("Rodin", 10000, 99, "Immortality",
                  "'He comes from the heavens above, be as one of the old archangels he wants nothing more than "
                  "to destroy those who have defied him.' He's tall, dark, and powerful foe. He is "
                  "nothing more than a weapon's blacksmith with an agenda to run his bar, 'Hell's Gate'. His "
                  "biggest client is a witch who knows her thing or two about hunting angels and she brings all "
                  "the goods that Rodin needs, while Rodin himself pours her a drink and starts creating her "
                  "weapons out of the Halos, Demon Blood, Ebony, and Angelic Tunes from the Heavens. He is "
                  "very picky when it comes to getting the job done!",
                  "Angelic Sword, Demon's Eye, Health Vials, Bar Keys")

print("Name: %s" % rodin.name)
print("Health: %s" % rodin.health)
print("Attack Power: %s" % rodin.attack)
print("Status Effect(s): %s" % rodin.status_effects)
print(rodin.physique)
print(rodin.information)
print("Inventory: %s" % rodin.inventory)