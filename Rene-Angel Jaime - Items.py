class Item(object):
    def __init__(self, name, info, value):
        self.name = name
        self.info = info
        self.value = value
        self.take = True
        self.drop = False

    def drop(self):
        self.take = False
        self.drop = True
        print("You take the item.")

    def take(self):
        self.take = True
        self.drop = False
        print("You take the item.")

    def sell(self):
        self.value += 100


class Weapon(Item):
    def __init__(self, name, info, durability, value):
        super(Weapon, self).__init__(name, info, value)
        self.attack = False
        self.durability = durability
        self.target = ()

    def damage(self, target):
        self.target = ()
        self.attack = True
        target.hp -= 100


class Consumable(Item):
    def __init__(self, name, info, effect, value):
        super(Consumable, self).__init__(name, info, value)
        self.use = False
        self.effect = effect

    def use(self):
        self.use = True
        print("You used this item")
        self.drop = True


bone_sword = Weapon("Bone Sword", "Created by the skeletal remains of fallen warriors.", 100, 25)
hp_potion = Consumable("Health Potion", "Use for injuries", "Healing", 75)
