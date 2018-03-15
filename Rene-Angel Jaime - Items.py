class Item(object):
    def __init__(self, name, info, value):
        self.name = name
        self.info = info
        self.value = value
        self.use = True

    def drop(self):
        self.drop()

    def sell(self):
        self.value += 100


class Weapon(Item):
    def __init__(self, name, info, range, attack, durability):
        super(Weapon, self).__init__(name, info)
        self.attack = attack
        self.durability = durability
        self.range = range
        self.target = ()

    def damage(self, target):
        self.target = ()
        self.attack = ()
        target.hp -= 100


class Consumable(Item):
    def __init__(self, name, info, use, effect):
        self.use = use
        self.effect = effect