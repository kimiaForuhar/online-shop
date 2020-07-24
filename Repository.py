class Rep:
    def __init__(self,id,capacity):
        self.id=id
        self.capacity=capacity
        self.goods={}

    # def getid(self):
    #     return self.id
    #
    # def getcapacity(self):
    #     return self.capacity

    def getfreecap(self):
        return self.capacity-sum(self.goods.values())
    #
    # def getgoods(self):
    #     return self.goods

    def addgood(self,good,amount):
        self.goods[good]+=amount

    def removegood(self,good,amount):
        self.goods[good]-=amount
