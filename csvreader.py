import csv
from math import ceil
from struct import pack

from hashmap import hashtable
from package import Package
from distance import getDistance, getAddressID, getTime
from truck import Truck

# Import csv file and insert package info into hash table.
# Time Complexity 0(n)
with open("package.csv") as csvfile:
    packagecsv = csv.reader(csvfile)
    for row in packagecsv:
        packageID = int(row[0])
        paddress = row[1]
        pcity = row[2]
        pstate = row[3]
        pzip = row[4]
        pdeadline = row[5]
        pweight = row[6]
        pmessage = row[7]

        packageItem = Package(packageID,paddress,pcity,pstate,pzip,pdeadline,pweight,pmessage)

        hashtable.insert(packageID,packageItem)


# Will use a version of Greedy algorithm.
# Will take in truck number as perameter to start delivery. Will originally set Hub address as current address and
# starting location. Will then run through every package on the truck and find which is closest location when compared
# the trucks current location. Will then travel to closest location and repeat until all packages on truck are delivered.
# Will also keep track of the miles traveled by each truck.
# Time Complexity 0(n^2)
def DeliverPackage(truck):
    route = []
    totalMiles = 0
    currentLocation = getAddressID('4001 South 700 East')
    start = getAddressID('4001 South 700 East')
    current_time = truck.start_time

    while truck.packages:
        min_dist = 1000
    
        for p1 in truck.packages:
            nextLocation = getAddressID(p1.address)
            dist = getDistance(currentLocation, nextLocation)        

            if min_dist > dist:
                min_dist = dist
                closest = p1

        currentLocation = getAddressID(closest.address)
        totalMiles += min_dist
        truckspeed = truck.speed/60
        min_elapsed = ceil(min_dist/truckspeed)
        deliverTime = getTime(min_dist, current_time, truck)
        current_time += min_elapsed
        closest.deliveryTime = deliverTime
        closest.on_truck = str(truck.truckID)
        route.append(closest)
        truck.packages.remove(closest)
    end = getAddressID(closest.address)
    totalMiles += getDistance(end,start)
    truck.totalMiles += totalMiles


# Manually load packages on to the trucks and then deliver packages with previous DeliverPackage method.
# Will return total mileage traveled by all three trucks.
# Run Time complexity of O(n)
def LoadAndDeliver():
    truck1 = Truck(1,500)
    truck2 = Truck(2,550)
    truck3 = Truck(3,660)
    totalMiles = 0
    for i in range(40):
        package = hashtable.search(i+1)
        ID = package.packageID
        if ID == 1 or ID == 4 or ID == 5 or ID == 13 or ID == 14 or ID == 15 or ID == 16 or ID == 19 or ID == 20 or ID == 29 or ID == 30 or ID == 31 or ID == 34 or ID == 37 or ID == 40:
            truck1.packages.append(package)
        if ID == 3 or ID == 6 or ID == 18 or ID == 25 or ID == 28 or ID == 32 or ID == 36 or ID == 38 or ID == 39:
            truck2.packages.append(package)
        if ID == 2 or ID == 7 or ID == 8 or ID == 9 or ID == 10 or ID == 11 or ID == 12 or ID == 17 or ID == 21 or ID == 22 or ID == 23 or ID == 24 or ID == 26 or ID == 27 or ID == 33 or ID == 35:
            truck3.packages.append(package)
    DeliverPackage(truck1)
    DeliverPackage(truck2)
    DeliverPackage(truck3)
    totalMiles += truck1.totalMiles
    totalMiles += truck2.totalMiles
    totalMiles += truck3.totalMiles
    
    return totalMiles