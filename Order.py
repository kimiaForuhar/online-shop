class Order:
    def __init__(self, id, customer):
        self.id = id
        self.customer = customer
        # self.status="pending"
        self.orders = {}
        self.price = 0
        self.discount = []

    def additem(self, good, amount):
        if good in self.orders:
            self.orders[good] += amount
        else:
            self.orders[good] = amount
        # self.price+=good.price

    def removeitem(self, good):
        self.orders.pop(good)
        # self.price-=good.price

    def calculateprice(self):
        for i in range(len(self.orders)):
            self.price += (self.orders[i] * self.orders.keys()[i].price)
        return self.price

    def adddiscount(self, discount):
        # self.discount.append(discount)
        self.price - self.price * (discount.getPercentage()) / 100