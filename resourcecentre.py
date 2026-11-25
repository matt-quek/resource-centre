# ============================================================
# Resource Centre System
# ============================================================

MENU_MIN = 0
MENU_MAX = 5 
TYPE_CAMERA = 1 
TYPE_LAPTOP = 2 
AVAILABLE = "Yes" 
LOANED = "No"

c = [
    ["C001", "Nikon COOLPIX L32", "Yes", ""],
    ["C002", "Canon PowerShot A4000 IS", "Yes", ""],
    ["C003", "Olympus TG-6 Tough", "Yes", ""],
]
l = [
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

def menu():
    x = -1
    # valid choices are 0 to 4 (0 = Quit)
    while not MENU_MIN <= x <= MENU_MAX:
        print("\n==============================================")
        print("RESOURCE CENTRE SYSTEM:")
        print("1. Add item")
        print("2. Display available items")
        print("3. Loan item")
        print("4. Return item")
        print("5. Show how many items are available")
        print("0. Quit")
        x = int(input("Enter your choice >"))
        if not MENU_MIN <= x <= MENU_MAX:
            print("Invalid choice, please enter again.\n")
    return x


def go():
    x = menu()
    while x != 0:

        if x == 1:
            print("")
            print("==============================================")
            print("Add an item")
            print("==============================================")
            print("\nItem types:")
            print("1. Digital Camera")
            print("2. Laptop")
            t = int(input("Enter option to select item type >"))
            if t == TYPE_CAMERA:
                tag = input("Enter asset tag >")
                desc = input("Enter description >")
                c.append([tag, desc, "Yes", ""])
                print("Digital camera added.")
            elif t == TYPE_LAPTOP:
                tag = input("Enter asset tag >")
                desc = input("Enter description >")
                l.append([tag, desc, "Yes", ""])
                print("Laptop added.")
            else:
                print("Invalid item type.")

        elif x == 2:
            print("")
            print("==============================================")
            print("Display available items")
            print("==============================================")
            for i in c:
                if i[2] == AVAILABLE:
                    print(i[0], i[1])
            for i in l:
                if i[2] == AVAILABLE:
                    print(i[0], i[1])

        elif x == 3:
            print("")
            print("==============================================")
            print("Loan an item")
            print("==============================================")
            print("\nItem types:")
            print("1. Digital Camera")
            print("2. Laptop")
            t = int(input("Enter option to select item type >"))
            if t == TYPE_CAMERA:
                for i in c:
                    if i[2] == AVAILABLE:
                        print(i[0], i[1])
                tag = input("Enter asset tag >")
                d = input("Enter due date >")
                for i in c:
                    if i[0] == tag:
                        if i[2] == AVAILABLE:
                            i[2] = LOANED
                            i[3] = d
                            print("Camera", tag, "loaned out.")
            elif t == TYPE_LAPTOP:
                for i in l:
                    if i[2] == AVAILABLE:
                        print(i[0], i[1])
                tag = input("Enter asset tag >")
                d = input("Enter due date >")
                for i in l:
                    if i[0] == tag:
                        if i[2] == AVAILABLE:
                            i[2] = LOANED
                            i[3] = d
                            print("Laptop", tag, "loaned out.")
            else:
                print("Invalid item type.")

        elif x == 4:
            print("")
            print("==============================================")
            print("Return an item")
            print("==============================================")
            print("\nItem types:")
            print("1. Digital Camera")
            print("2. Laptop")
            t = int(input("Enter option to select item type >"))
            if t == TYPE_CAMERA:
                tag = input("Enter asset tag >")
                for i in c:
                    if i[0] == tag:
                        i[2] = AVAILABLE
                        i[3] = ""
                        print("Camera", tag, "returned.")
            elif t == TYPE_LAPTOP:
                tag = input("Enter asset tag >")
                for i in l:
                    if i[0] == tag:
                        i[2] = AVAILABLE
                        i[3] = ""
                        print("Laptop", tag, "returned.")
            else:
                print("Invalid item type.")

        elif x == 5:
            print("Cameras available:", count_available(c))
            print("Laptops available:", count_available(l))

        else:
            print("Invalid choice.")

        x = menu()

    print("Good bye.")


def tag_unused():
    return "___never___"


go()
