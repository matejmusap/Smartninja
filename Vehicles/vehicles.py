class Vehicle:
    def __init__(self, brand, model, kilometers, general_service):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.general_service = general_service

    def name_of_vehicle(self):
        return self.brand + " " + self.model

def list_all_vehicless(vehicles):
    for index, vehicle in enumerate(vehicles):
        print vehicle.brand
        print vehicle.model
        print vehicle.kilometers
        print vehicle.general_service
        print ""

    if not vehicles:
        print "You don't have any vehicles in your contact list."

def add_vehicle(vehicles):
    brand = raw_input("Please enter brand of vehicle:")
    model = raw_input("Please enter model of vehicle:")
    kilometers = raw_input("Please enter kilometers done so far:")
    general_service = raw_input("Please enter year of general service:")

    new = Vehicle(brand, model, kilometers, general_service)
    vehicles.append(new)

    print ""
    print new.name_of_vehicle() + " was successfully added to your vehicle list."

def select_vehicle(vehicles):
    print "Select the number of the vehicle you'd like to edit:"

    for index, vehicle in enumerate(vehicles):
        print str(index) + ") " + vehicle.name_of_vehicle()

    print ""

def edit_kilometars(vehicle):
    select_vehicle(vehicle)
    selected_id = raw_input("What vehicle would you like to edit? (enter ID number): ")
    vehicle = vehicle[int(selected_id)]

    new_kilometers = raw_input("Please enter a updated kilometers for %s: " % vehicle.name_of_vehicle())
    vehicle.kilometers = new_kilometers

    print ""
    print "Kilometers updated."

def edit_general_service(vehicle):
    select_vehicle(vehicle)
    selected_id = raw_input("What vehicle would you like to edit? (enter ID number): ")
    vehicle = vehicle[int(selected_id)]

    new_general_service = raw_input("Please enter year of general service for %s: " % vehicle.name_of_vehicle())
    vehicle.general_service = new_general_service

    print ""
    print "Year of general service updated."

def main():
    print "Welcome to your Contact List"
    vehicles = []

    while True:
        print ""
        print "Please choose one of these options:"
        print "a) See all your vehicles"
        print "b) Add a new vehicles"
        print "c) Edit Kilometars"
        print "d) Edit General Service Data"
        print "e) Quit the program."
        print ""

        selection = raw_input("Enter your selection (a, b, c, d or e): ")
        print ""

        if selection.lower() == "a":
            list_all_vehicless(vehicles)
            with open("vehicles.txt", "w") as vehicles_file:
                vehicles_file.write("All vehicles:\n")
                for Vehicle in vehicles:
                    vehicles_file.write("%s %s\n%s\n%s\n" % (Vehicle.brand, Vehicle.model, Vehicle.kilometers, Vehicle.general_service))
                vehicles_file.write("Feel free to add new vehicle or update existing vehicles!")
        elif selection.lower() == "b":
            add_vehicle(vehicles)
        elif selection.lower() == "c":
            edit_kilometars(vehicles)
        elif selection.lower() == "d":
            edit_general_service(vehicles)
        elif selection.lower() == "e":
            print "Thank you for using Contact List. Goodbye!"
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue

if __name__ == "__main__":
    main()