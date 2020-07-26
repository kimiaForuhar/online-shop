class Rep:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.goods = {}

    def getfreecap(self):
        return self.capacity - sum(self.goods.values())

    def addgood(self, good, amount):
        self.goods[good] += amount

    def removegood(self, good, amount):
        self.goods[good] -= amount