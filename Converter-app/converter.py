def main():
    print "Hello user!"
    print "Here you can convert kilometers to miles and miles to kilometers"
    print "1 km = 0.621371192 miles"
    print "1 mile = 1.609344 kilometers"
    again = "y"
    try:
        while again == "y":
            dist = float(raw_input("Enter distance: "))
            unit = raw_input("Enter Unit of measurement(km or miles): ")
            print str(dist) + " " + unit
            if unit == "km":
                print convert_km(dist)
                again = raw_input("Do you want to convert another distance?(Y/N):")
            elif unit == "miles":
                print convert_miles(dist)
                again = raw_input("Do you want to convert another distance?(Y/N):")
            elif unit != "km" and unit != "miles":
                print "Write distance measure unit!(km or miles)"
                again = raw_input("Do you want to convert another distance?(Y/N):")
            if again == "n":
                print "Thank you for use converter!"
            while again != "y" and again != "n":
                print "Please enter y or n"
                again = raw_input("Do you want to convert another distance?(Y/N):")
                if again == "n":
                    print "Thank you for use converter!"
    except Exception as e:
        print "Please enter a whole number."


def convert_km(dist):
    result = dist * 0.621371192
    result_round = ("%.2f" % result)
    return str(result_round) + "km"

def convert_miles(dist):
    result = dist * 1.609344
    result_round = ("%.2f" % result)
    return str(result_round) + "miles"

def convert(dist, unit):
    try:
        if unit == "km":
            result_str = convert_km(dist)
        elif unit == "miles":
            result_str = convert_miles(dist)
        else:
            result_str = "Please enter correct unit"
        return result_str
    except Exception as e:
        return "Please enter a whole number."

if __name__ == "__main__":
    main()


