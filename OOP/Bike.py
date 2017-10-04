class Bike(object):

    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0 #set miles to '0'

    def displayInfo(self):
		print self.price, self.max_speed, self.miles
		return self

    def ride(self):
        self.miles += 10
        print "Riding", self.miles
        return self

    def reverse(self):
        self.miles -= 5
        print "Reversing", self.miles
        return self

    def Bike_print(self):
        print('Bike Price: ' + str(self.price))
        print('Max Speed: ' + str(self.max_speed))
        print('Miles: ' + str(self.miles))

# Have the first instance ride three times, reverse once and have it displayInfo().
# Have the second instance ride twice, reverse twice and have it displayInfo(). 
# Have the third instance reverse three times and displayInfo().
    
bike1 = Bike(200, "25mph").ride().ride().ride().reverse().displayInfo()
# print
bike2 = Bike(300, "15mph").ride().ride().reverse().reverse().displayInfo()
bike3 = Bike(1000, "30mph").reverse().reverse().reverse().displayInfo()


# print









# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...