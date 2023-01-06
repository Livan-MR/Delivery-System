# Student: Livan Martinez
# Student ID: 001520260

from csvreader import LoadAndDeliver
from hashmap import hashtable

# Calls method to load and deliver trucks and will return total miles traveled by all trucks.
miles = LoadAndDeliver()


# Main Class to run program
# Time Complecity 0(n)
class Main:

    # Initialize UI for program. Will inform user that typing quit will exit program and promp user to enter a time
    # to retrieve packages.
    userInput = ''
    
    print("Type quit to exit program\n")
    print("Total milage after delivery is", miles, "miles.\n")
    userInput = input("Press 1 for all package info\nPress 2 to look up package ID\n")

    # As long as user entered a correct time and did not type quit, We will loop through the hashtable and compare
    # the user's requested time with the status of the packages at that requested time. Once we have looped through
    # all the packages in the and found their current status at the requested time we will loop and print the 
    # information for the packages and reveal their status at the requested time. Finally we will set the user input
    # to quit in order to exit program.

    if userInput == '1':

        userInput = input("\nEnter a time to retrieve all package data. (HH:MM:SS)\n")

        while userInput != 'quit':

            print(f"\nShowing all package data for {userInput}")

            for i in range(40):
                    package = hashtable.search(i + 1)
                    packageTime = package.deliveryTime
                    packageTimeSplit = packageTime.split(':')
                    userTime = userInput.split(':')
                    packageHour = int(packageTimeSplit[0])
                    packageMin = int(packageTimeSplit[1])
                    userHour = int(userTime[0])
                    userMin = int(userTime[1])
                    if userHour > packageHour:
                        package.deliveryStatus = 'Delivered'
                        
                        #If time is past 10:20 and delivered correct address and zip of package 9
                        if package.deliveryStatus == 'Delivered' and package.packageID == 9:
                            package.address = '410 S State St'
                            package.zip = "84111"
                        
                    elif userHour == packageHour and userMin >= packageMin:
                        package.deliveryStatus = 'Delivered'

                    elif ((userHour * 60) + userMin) >= 480 and ((userHour * 60) + userMin) <= 545 and i == 5 or i == 24 or i == 27 or i == 31:
                        package.deliveryStatus = 'At Hub'

                    elif ((userHour * 60) + userMin) >= 480:
                        package.deliveryStatus = 'En route'

                    #If time is past 10:20 correct address and zip of package 9
                        if ((userHour * 60) + userMin) >= 620 and i == 8:
                            package.address = '410 S State St'
                            package.zip = "84111"

                    else:
                        package.deliveryStatus = 'At Hub'
            if userMin < 10:
                userMin = int('0{}'.format(userMin))

            for i in range(40):
                package = hashtable.search(i + 1)
                if package.deliveryStatus == 'Delivered':
                    print('Package:', package, 'was on truck', package.on_truck)
                elif package.deliveryStatus == 'En route':
                    print('Package:', package, ', on truck', package.on_truck)
                elif package.deliveryStatus == 'At Hub':
                    print('Package:', package, ', will load on truck', package.on_truck)
    
            userInput = 'quit'

    # As long as user entered a correct time and a valid package ID and did not type quit, We will loop through the 
    # hashtable and compare the user's requested time with the status of the packages at that requested time. Once 
    # we have looped through all the packages We will search the hashtable for the package ID that the user 
    # requested and print package info. Finally we will set the user input to quit in order to exit program.

    if userInput == '2':

        usertimestamp = input("\nEnter a time to retrieve all package data. (HH:MM:SS)\n")
        packageID = input('\nEnter an ID from 1 to 40\n')

        while userInput != 'quit':

            print(f"\nShowing all package data for package {packageID} at {usertimestamp}")

            for i in range(40):
                    package = hashtable.search(i + 1)
                    packageTime = package.deliveryTime
                    packageTimeSplit = packageTime.split(':')
                    userTime = usertimestamp.split(':')
                    packageHour = int(packageTimeSplit[0])
                    packageMin = int(packageTimeSplit[1])
                    userHour = int(userTime[0])
                    userMin = int(userTime[1])
                    if userHour > packageHour:
                        package.deliveryStatus = 'Delivered'

                        #If time is past 10:20 and package delivered correct address and zip of package 9
                        if package.deliveryStatus == 'Delivered' and int(packageID) == 9:
                            package.address = '410 S State St'
                            package.zip = "84111"
                        
                    elif userHour == packageHour and userMin >= packageMin:
                        package.deliveryStatus = 'Delivered'

                    elif ((userHour * 60) + userMin) >= 480 and ((userHour * 60) + userMin) <= 545 and i == 5 or i == 24 or i == 27 or i == 31:
                        package.deliveryStatus = 'At Hub'
                    
                    elif ((userHour * 60) + userMin) >= 480:
                        package.deliveryStatus = 'En route'
                    
                    #If time is past 10:20 correct address and zip of package 9
                        if ((userHour * 60) + userMin) >= 620 and i == 8:
                            package.address = '410 S State St'
                            package.zip = "84111"

                    else:
                        package.deliveryStatus = 'At Hub'
            
            package = hashtable.search(int(packageID))

            if package.deliveryStatus == 'Delivered':
                print('\nPackage:', package, 'on truck', package.on_truck, '\n')
            elif package.deliveryStatus == 'En route':
                print('\nPackage:', package, ', on truck', package.on_truck, '\n')
            elif package.deliveryStatus == 'At Hub':
                print('\nPackage:', package, ', Loaded on truck', package.on_truck, '\n')

            userInput = 'quit'