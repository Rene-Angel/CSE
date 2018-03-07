class Character(object):
    def __init__(self, name, health, status, height, weight, race, description, inventory):
        self.name = name
        self.health = health
        self.status = status
        self.physique = height, weight, race
        self.description = description
        self.inventory = inventory


first_person = Character("Rodin", 10000, "ally", "6'5 ft", "230.5 lbs", "Archangel",
                         "'He comes from the heavens above, be as one of the old archangels he wants nothing more than"
                         " to destroy those who have defied him.' He's tall, dark, and of course handsome. He is "
                         "nothing more than a weapon's blacksmith with an agenda to run his bar, 'Hell's Gate'. His "
                         "biggest client is a witch who knows her thing or two about hunting angels and she brings all "
                         "the goods that Rodin needs, while Rodin himself pours her a drink and starts creating her "
                         "weapons out of the Halos, Demon Blood, Ebony, and Angelic Tunes from the Heavens. He is "
                         "very picky when it comes to getting the job done!",
                         "Inventory: Angel's Sword, Health Vials, Bar Key")

print(first_person.name)
print(first_person.health)
print(first_person.status)
print(first_person.physique)
print(first_person.description)
print(first_person.inventory)