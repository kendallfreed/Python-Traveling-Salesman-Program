# Package object class
class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def package_status_update(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.status = "Delivered"
        elif self.departure_time < convert_timedelta and self.departure_time < self.delivery_time:
            self.status = "On Truck"
            if self.ID == 9:
                self.address = "410 S State St"
        else:
            self.status = "At Hub"

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city,
                                                   self.state, self.zipcode, self.deadline,
                                                   self.weight, self.status)

