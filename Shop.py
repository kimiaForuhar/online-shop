class Shop:
    def __init__(self, name):
        self.name = name
        self.customerslist = []
        self.reps = []
        self.income = 0
        self.goods = []
        self.discount = []

    def sort_reps(self):
        rep_sorted = [r.capacity for r in self.reps]

    def addcustomers(self, customers):
        self.customerslist.append(customers)

    def addrep(self, rep):
        self.reps.append(rep)

    def setincome(self, income):
        self.income += income

    def setgood(self, good):
        self.goods.append(good)

    def increamentGood(self, good, amount):
        #
        for i in range(len(self.reps)):
            if amount <= self.reps[i].capacity:
                self.reps[i].addgood(good, amount)
                break

    def addDiscount(self, discount):
        self.discount.append(discount)
