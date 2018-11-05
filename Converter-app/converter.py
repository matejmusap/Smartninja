print "Hello user!"
print "Here you can convert kilometers to miles and miles to kilometers"
again = "y"
try:
    while again == "y":
        dist = float(raw_input("Enter distance: "))
        unit = raw_input("Enter Unit of measurement(km or miles): ")
        print str(dist) + " " + unit
        if unit == "km":
            print "1 km = 0.621371192 miles"
            result = dist * 0.621371192
            print str(result) + " miles"
            again = raw_input("Do you want to convert another distance?(Y/N):")
        elif unit == "miles":
            result = dist * 1.609344
            print "1 mile = 1.609344 kilometers"
            print str(result) + " km"
            again = raw_input("Do you want to convert another distance?(Y/N):")
        elif unit != "km" and unit != "miles":
            print "Write distance measurment unit!(km or miles)"
            again = raw_input("Do you want to convert another distance?(Y/N):")
    if again == "n":
        print "Thank you for use converter!"
    elif again != "y" and again != "n":
        print "Please enter y or n"
        again = raw_input("Do you want to convert another distance?(Y/N):")
except Exception as e:
    print "Please enter a whole number."

