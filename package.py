# Class to structure package data from csv.

class Package:
    def __init__(self, packageID, address, city, state, zip, deadline, mass, note, status=''):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.note = note
        self.deliveryStatus = status
        self.deliveryTime = ''
        self.on_truck = ''

    # Converts packages to readable strings
    def __str__(self):
        return ('{}, {}, {}, {} {}, {}, {}, {},'
                ' Delivery time {}, Status of package: {}'.format(self.packageID, self.address, self.city,
                                 self.state, self.zip, self.mass, self.note, self.deadline,
                                 self.deliveryTime, self.deliveryStatus))