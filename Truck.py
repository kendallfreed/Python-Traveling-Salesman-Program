#Truck object class
class Truck:
    def __init__(self, max_packages, speed, packages_on_board, mileage, address, departure_time) :
        self.max_packages = max_packages
        self.speed = speed
        self.packages_on_board = packages_on_board
        self.mileage = mileage
        self.address = address
        self.departure_time = departure_time
        self.time_between_deliveries=departure_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.max_packages, self.speed, self.load,
                                               self.packages_on_board, self.mileage, self.address, self.departure_time)

