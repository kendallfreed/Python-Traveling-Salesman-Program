#Student ID: 010213248
#Name: Kendall Freed
import csv
import Truck
import datetime

from HashTable import ChainingHashTable
from Package import Package

#Open and read Distance File and add to a list
with open ("CSV_Files/Distance_File.csv") as distance_file:
    CSV_Distance = csv.reader(distance_file)
    CSV_Distance = list(CSV_Distance)

#Open and read Package File and add to a list
with open ("CSV_Files/Package_File.csv") as package_file:
    CSV_Package = csv.reader(package_file)
    CSV_Package = list(CSV_Package)

#Open and read Address File and add to a list
with open ("CSV_Files/Address_File.csv") as address_file:
    CSV_Address = csv.reader(address_file)
    CSV_Address = list(CSV_Address)

#Creates hash table instance
package_hash_table = ChainingHashTable()

#Create Truck objects, manually loading the package by package #'s
#Truck 1 leaves first at the earliest time, 8AM
truck_1 = Truck.Truck(16, 18,
                      [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0, "4001 South 700 East",
                      datetime.timedelta(hours = 8))
#Truck 2 leaves second
truck_2 = Truck.Truck(16, 18,
                      [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0, "4001 South 700 East",
                      datetime.timedelta(hours = 9, minutes=5))
#Truck 3 leaves at 10:20am when Package 9 address updates
truck_3 = Truck.Truck(16, 18,
                      [2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0, "4001 South 700 East",
                      datetime.timedelta(hours = 10, minutes = 20))

#Read Packages from Package CSV File and create Hash table to insert packages
def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_deadline = package[5]
            package_weight = package[6]
            package_status = "At Hub"
            package = Package(package_id, package_address, package_city, package_state, package_zipcode,
                              package_deadline, package_weight, package_status)
            package_hash_table.insert(package_id, package)

#Look up package info
def look_up_package(package_id):
    print(package_hash_table.search(package_id))

#Return distance between two addresses
def distance_between(address_1, address_2):
   distance_data = CSV_Distance[address_1][address_2]
   #Due to table's design, with distances displayed cascading down, if a blank cell is found it will flip the
   #x and y axis so that it will give the correct value
   if distance_data == '':
       distance_data = CSV_Distance[address_2][address_1]
   return float(distance_data)

#Take address and return it as the integer/key from Address File CSV
def address_int(address):
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])

#Load packages into hash table by calling function
load_package_data("CSV_Files/Package_File.csv", package_hash_table)

#Greedy/Nearest Neighbor Algorithm to find nearest option to go to next for package delivery
def package_delivery_algorithm (truck):
    #Packages moved to array of pending state while waiting to be delivered
    pending_packages = []
    for package_id in truck.packages_on_board:
        package = package_hash_table.search(package_id)
        pending_packages.append(package)
    #Clear the packages from the truck so they can be loaded from algorithm
    truck.packages_on_board.clear()


    #Loop through pending packages to load nearest package into truck packages list and update truck details
    while len(pending_packages) > 0:
        next_address = 2000
        next_package = None
        #Find closest package and add to Truck packages list
        for package in pending_packages:
            if distance_between(address_int(truck.address), address_int(package.address)) <= next_address:
                next_address = distance_between(address_int(truck.address), address_int(package.address))
                next_package = package
        truck.packages_on_board.append(next_package.ID)
        pending_packages.remove(next_package)
        #Update truck's next address and mileage
        truck.address = next_package.address
        truck.mileage += next_address
        #Update truck's time between deliveries, departure, and delivery time
        truck.time_between_deliveries += datetime.timedelta(hours= (next_address / 18))
        next_package.delivery_time = truck.time_between_deliveries
        next_package.departure_time = truck.departure_time

#Send trucks out
package_delivery_algorithm(truck_1)
package_delivery_algorithm(truck_2)
package_delivery_algorithm(truck_3)

#Calculate total mileage of trucks
total_mileage = truck_1.mileage + truck_2.mileage + truck_3.mileage

#User Interface to view status of packages based on time entered
class Main:
    print(truck_3.departure_time)
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Western Governor's University Parcel Service (WGUPS) Routing Program")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                   ______________________________________________________")
    print("                  |                                                      |")
    print("             /    |                                                      |")
    print("            /---, |                                                      |")
    print("       -----# ==| |                                                      |")
    print("       | :) # ==| |                                                      |")
    print("  -----'----#   | |______________________________________________________|")
    print(" |)___()  '#   |______====____   \___________________________________|")
    print("[_/,-,\'--'------ //,-,  ,-,\\\   |/             //,-,  ,-,  ,-,\\ __#")
    print(" ( 0 )|===******||( 0 )( 0 )||-  o              '( 0 )( 0 )( 0 )||")
    print("----'-'--------------'-'--'-'-----------------------'-'--'-'--'-'--------------")
    print("Total Mileage of all the trucks is: {} miles".format(total_mileage))
    print("\tMileage of Truck 1 {}".format(round(truck_1.mileage, 1)))
    print("\tMileage of Truck 2 {}".format(truck_2.mileage))
    print("\tMileage of Truck 3 {}".format(truck_3.mileage))
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nTo begin, enter a time (using HH:MM:SS).")
    print("\nType Exit to exit the program at any time.")
    user_input = input("\nEnter time here:")
    while user_input != "Exit":
        (user_hours, user_minutes, user_seconds) = user_input.split(":")
        user_time = datetime.timedelta(hours = int(user_hours), minutes = int(user_minutes), seconds = int(user_seconds))
        print("\nSelect from the following options to view delivery status:")
        print("\tReport - See report of all packages delivered at your entered time.")
        print("\tSingle - Can view a single package status after inputting package ID.")
        print("\tType Exit to exit the program at any time.")
        user_choice = input("\nEnter choice here:")
        if user_choice == "Single":
            user_package_id = input("\nEnter a package ID (1 - 41) to view a single package status: ")
            #Check if package ID entered is a number and within range of valid IDs
            if user_package_id.isdigit() and int(user_package_id) >= 1 and user_package_id.isdigit() and int(user_package_id) <= 41:
                pacakge = package_hash_table.search(int(user_package_id))
                print(str(pacakge))
            elif user_package_id == "Exit":
                exit()
            else:
                print("Invalid package ID, exiting program.")
                exit()
        elif user_choice == "Report":
            for package_id in range(1, 41):
                package = package_hash_table.search(package_id)
                package.package_status_update(user_time)
                print(str(package))
        elif user_choice == "Exit":
            print("Exiting program.")
            exit()
        else:
            print("Invalid input, exiting program.")
            exit()
