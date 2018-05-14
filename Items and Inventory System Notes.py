class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class InvItem(object):
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount


class Container(object):
    def __init__(self):
        self.inventory = []

    def addtoinv(self, item):
        self.inventory.append(item)
