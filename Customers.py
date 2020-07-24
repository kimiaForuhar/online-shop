class Customers:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.balance=0
        self.orderslist=[]
        self.saved=[]
        self.discounted=False

    # def getname(self):
    #     return  self.name
    #
    # def getid(self):
    #     return self.id
    #
    # def getbalance(self):
    #     return self.balance

    def setbalance(self,amount):
        self.balance+=amount

    def addorder(self,order):
        self.orderslist.append(order)

    # def gettotalorders(self):
    #     return self.orderslist

    def pendingorders(self):
        return self.orderslist - self.saved

    def savedorders(self):
        return self.saved

    def submitorder(self,order):
        self.saved.append(order)