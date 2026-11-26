# ============================================================
# Resource Centre System
# ============================================================

MENU_MIN = 0
MENU_MAX = 5 
TYPE_CAMERA = 1 
TYPE_LAPTOP = 2 
AVAILABLE = "Yes" 
LOANED = "No"

cameras = [
    ["C001", "Nikon COOLPIX L32", "Yes", ""],
    ["C002", "Canon PowerShot A4000 IS", "Yes", ""],
    ["C003", "Olympus TG-6 Tough", "Yes", ""],
]
laptops = [
    ["L001", "Lenovo Yoga Pro 7", "Yes", ""],
    ["L002", "ASUS Vivobook", "Yes", ""],
    ["L003", "HP Pavilion Plus 14", "Yes", ""],
]

def count_available(items):
    count = 0
    for item in items:
        if item[2] == "Yes":
            count = count + 1
    return count

def print_header(message):
    
    print("")
    print("==============================================")
    print(message)
    print("==============================================")


def menu():
    choice = -1
    # valid choices are 0 to 4 (0 = Quit)
    while not MENU_MIN <= choice <= MENU_MAX:
        print("\n==============================================")
        print("RESOURCE CENTRE SYSTEM:")
        print("1. Add item")
        print("2. Display available items")
        print("3. Loan item")
        print("4. Return item")
        print("5. Show how many items are available")
        print("0. Quit")
        choice = int(input("Enter your choice >"))
        if not MENU_MIN <= choice <= MENU_MAX:
            print("Invalid choice, please enter again.\n")
    return choice


def go():
    choice = menu()
    while choice != 0:

        if choice == 1:
            print_header("Add an item")
            print("\nItem types:")
            print("1. Digital Camera")
            print("2. Laptop")
            item_type = int(input("Enter option to select item type >"))
            if item_type == TYPE_CAMERA:
                tag = input("Enter asset tag >")
                desc = input("Enter description >")
                cameras.append([tag, desc, "Yes", ""])
                print("Digital camera added.")
            elif item_type == TYPE_LAPTOP:
                tag = input("Enter asset tag >")
                desc = input("Enter description >")
                laptops.append([tag, desc, "Yes", ""])
                print("Laptop added.")
            else:
                print("Invalid item type.")

        elif choice == 2:
            print_header("Display available items")
            for i in cameras:
                if i[2] == AVAILABLE:
                    print(i[0], i[1])
            for i in laptops:
                if i[2] == AVAILABLE:
                    print(i[0], i[1])

        elif choice == 3:
            print_header("Loan an item")
            print("\nItem types:")
            print("1. Digital Camera")
            print("2. Laptop")
            item_type = int(input("Enter option to select item type >"))
            if item_type == TYPE_CAMERA:
                for i in cameras:
                    if i[2] == AVAILABLE:
                        print(i[0], i[1])
                tag = input("Enter asset tag >")
                due_date = input("Enter due date >")
                for i in cameras:
                    if i[0] == tag:
                        if i[2] == AVAILABLE:
                            i[2] = LOANED
                            i[3] = due_date
                            print("Camera", tag, "loaned out.")
            elif item_type == TYPE_LAPTOP:
                for i in laptops:
                    if i[2] == AVAILABLE:
                        print(i[0], i[1])
                tag = input("Enter asset tag >")
                due_date = input("Enter due date >")
                for i in laptops:
                    if i[0] == tag:
                        if i[2] == AVAILABLE:
                            i[2] = LOANED
                            i[3] = due_date
                            print("Laptop", tag, "loaned out.")
            else:
                print("Invalid item type.")

        elif choice == 4:
            print_header("Return an item")
            print("\nItem types:")
            print("1. Digital Camera")
            print("2. Laptop")
            item_type = int(input("Enter option to select item type >"))
            if item_type == TYPE_CAMERA:
                tag = input("Enter asset tag >")
                for i in cameras:
                    if i[0] == tag:
                        i[2] = AVAILABLE
                        i[3] = ""
                        print("Camera", tag, "returned.")
            elif item_type == TYPE_LAPTOP:
                tag = input("Enter asset tag >")
                for i in laptops:
                    if i[0] == tag:
                        i[2] = AVAILABLE
                        i[3] = ""
                        print("Laptop", tag, "returned.")
            else:
                print("Invalid item type.")

        elif choice == 5:
            print("Cameras available:", count_available(cameras))
            print("Laptops available:", count_available(laptops))

        else:
            print("Invalid choice.")

        choice = menu()

    print("Good bye.")



go()
