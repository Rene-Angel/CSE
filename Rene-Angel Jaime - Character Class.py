class Character(object):
    def __init__(self, name, health, attack, stats, inventory):
        self.name = name
        self.health = health
        self.stats = stats
        self.inventory = inventory
        self.attack = attack
        self.damage = damage

    def damage(self, target):
        if target.damage(self.attack):
            print("You took Damage.")
            self.health -= self.attack

    def take_damage(self):
        self.health(attack)


player = Character("Rodin", 100, 25, None, None)
enemy = Character("Angel", 50, 10, None, None)

(player.attack(enemy))
(enemy.attack(player))
print(self.health)
