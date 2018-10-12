print "Restaurant menu"

menu = {}

while True:
    dish = raw_input("Dish: ")
    price = raw_input("Price: ")
    menu[dish] = price
    new_dish = raw_input("Add new dish?(yes/no): ")
    if new_dish.lower() == "no":
        print menu
        break
with open("menu.txt", "w+") as menu_file:
    menu_file.write("Menu:\n")
    for dish in menu:
        menu_file.write("%s: %s kn\n" % (dish, menu[dish]))
    menu_file.write("THANKS FOR YOUR ORDER\n")
print "THANKS FOR YOUR ORDER"
