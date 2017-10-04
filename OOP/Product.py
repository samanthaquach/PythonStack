class Product(object):

    def __init__(self, price, itemName, weight, brand, cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        if price == 0:
            self.status = "sold"
        if cost == str("return"):
            self.status = "return"
            self.price = 0
        if cost == str("returning with box"):
            self.status = "like new"
        if cost <= str("returning open box"):
            self.price = (self.price - (self.price * 0.2))
    
    def calculateStateTax(self):
        state_tax = 0.05
        print 'Total with tax $'+ str((self.price * state_tax) + self.price)
        return self

    def displayInfo(self):
        print('Item: ' + str(self.itemName))
        print('Product Price: $' + str(self.price))
        print('Weight: ' + str(self.weight))
        print('Brand: ' + str(self.brand))
        print('Cost: $' + str(self.cost))
        print self.status
        return self

doll_house = Product(100,"Doll House","5lbs","Rockstar", "return").displayInfo().calculateStateTax()
# print doll_house