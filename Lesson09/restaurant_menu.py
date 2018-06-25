print "Welcome to the restaurant menu program."

menu = {}

while True:
    dish_name = raw_input("Please enter the name of the dish: ")
    dish_price = float(raw_input("Enter the price for '%s': " % dish_name))
    menu[dish_name] = dish_price

    new = raw_input("Would you like to enter new dish? (yes/no) ")

    if new.lower() == "no":
        break

print "Menu: %s" % menu

with open("menu.txt", "w+") as menu_file:  # open the file for writing and overwrite the previous file (w+)
    for dish in menu:
        menu_file.write("%s, %s EUR\n" % (dish, menu[dish]))

print "Goodbye!"
