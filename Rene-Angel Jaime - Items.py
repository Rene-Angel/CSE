class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.take = True
        self.drop = False
        self.health = 1000
        self.target_health = 1000

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
    def __init__(self, name, attack, value):
        super(Weapon, self).__init__(name, value)
        self.attack = attack

    def attack(self):
        self.attack = True
        self.target_health -= self.attack


class Ammunition(Item):
    def __init__(self, name, damage, amount):
        super(Ammunition, self).__init__(name, value)
        self.damage = damage
        self.amount = amount

    def fire(self):
        self.target_health -= self.damage


class Consumable(Item):
    def __init__(self, name, effect, value):
        super(Consumable, self).__init__(name, value)
        self.use = False
        self.effect = effect

    def use(self):
        self.use = True
        print("You used this item")
        self.health += self.effect
        self.effect = True
        self.drop = True


class Bone_Sword(Weapon):
    def __init__(self):
        super(Bone_Sword, self).__init__("Bone Sword", 5, 10)


class War_Axe(Weapon):
    def __init__(self):
        super(War_Axe, self).__init__("War Axe", 15, 20)


class X_Bow(Weapon):
    def __init__(self):
        super(X_Bow, self).__init__("Cross Bow", 20, 40)


class Arrows(Ammunition):
    def __init__(self):
        super(Arrows, self).__init__("Arrows", 25, 50)


class Health_Potion(Consumable):
    def __init__(self):
        super(Health_Potion, self).__init__("Health Potion", 100, 100)


class Apple(Consumable):
    def __init__(self):
        super(Apple, self).__init__("Apple", 5, 1)


class Branch(Weapon):
    def __init__(self):
        super(Branch, self).__init__("Tree Branch", 10, 1)


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__("Dagger", 15, 10)


class Egg(Consumable):
    def __init__(self):
        super(Egg, self).__init__("Egg", 10, 5)


class Long_Bow(Ammunition):
    def __init__(self):
        super(Long_Bow, self).__init__("Long Bow", 20, 30)


class Stick(Item):
    def __init__(self):
        super(Stick, self).__init__("Stick", 0)

    def use(self):
        print("It's just a stick what more do you want?")


