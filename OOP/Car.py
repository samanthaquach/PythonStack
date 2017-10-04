# class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    # print ("finished")

    def display_all(self):
        print self.price, self.speed, self.fuel, self.mileage, self.tax
        return self

# Create a class called Car. 
# allow the user to specify the following attributes: price, speed, fuel, mileage. 
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

car1 = Car(2000,"15mph","Full","20mpg").display_all()
car2 = Car(20000,"18mph","None","50mpg").display_all()
car3 = Car(50000,"15mph","Full","20mpg").display_all()
car4 = Car(6000,"15mph","None","20mpg").display_all()
car5 = Car(25000,"15mph","Full","20mpg").display_all()
car6 = Car(9000,"15mph","Full","20mpg").display_all()
# print car1.price
# print
# print car1