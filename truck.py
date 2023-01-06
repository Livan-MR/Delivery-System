# Class for trucks that will carry packages. Will structure info such as truck number, what packages are loaded
# on each truck, the speed of the truck being 18mph, total miles traveled by truck and time to start deliveries.

class Truck:
    def __init__(self, truckID, start_time):
        self.truckID = truckID
        self.packages = []
        self.speed = 18
        self.start_time = start_time
        self.totalMiles = 0