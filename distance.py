import csv

# Import csv file info and create a table to store data.
# Time Complexity: 0(n)
with open("distance.csv") as csvfile:
    distancecsv = csv.reader(csvfile)
    distList = []
    for row in distancecsv:
        distList.append(row)

# Import csv file info and create a table to store data.
# Time Complexity: 0(n)
with open("address.csv") as csvfile:
    addresscsv = csv.reader(csvfile)
    locationList = []
    for row in addresscsv:
        locationList.append(row)


# Method  to search through address matrix and return the id of the given address. 
# Space Time Complexity: 0(n)
def getAddressID(address):
    address = address
    addressID = 0
    for location in locationList:
        if location[2] == address:
            addressID = int(location[0])
    return addressID


# Method to search the distance matrix. The user will first use the getAddressID method to find address ID's.
# Then we will compare the two address with the distance matrix to find the distance in miles between the two
# given addresses.
# Time complexity 0(n)
def getDistance(row,col):
    distance = distList[row][col]
    if distance == '':
        distance = distList[col][row]
    return float(distance)


# Method to find the delivery time of a package.
# Will take distance needed to travel from one address to the next and divide it by the speed of the truck (18mph),
# then multiply by 60 to convert into minutes. Add the time the truck was originally at to the amount of elapesed time
# and we will get the delivery time in minutes. We will then have to convert the minutes into a normal formatted time that
# can be read by the user.
# Time Complexity: 0(1)
def getTime(distance,start_time,truck):
    min_elapsed = int(distance / truck.speed) * 60
    depart_time = start_time + min_elapsed
    newHours = int(depart_time / 60)
    minutes = int(depart_time - (newHours * 60))
    if minutes < 10:
        newMinutes = '0' + str(minutes)
        minutes = newMinutes
    deliver_time = str(newHours) + ':' + str(minutes)
    truck.start_time += min_elapsed

    return deliver_time