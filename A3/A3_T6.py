def main():

    print("Program starting.")
    print("Welcome to the unit converter program!")
    print("Follow the menu instructions below.")
    print()

    print("Options:")
    print("1 - Length")
    print("2 - Weight")
    print("3 - Exit")

    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Unknown option.")
        print()
        print("Program ending.")
        return
    if choice == 1:
        
        print("\nLength options:")
        print("1 - Meters to kilometers")
        print("2 - Kilometers to meters")
        print("0 - Exit") 
        
        try:
            choice2 = int(input("Your choice: "))
        except ValueError:
            print("Unknown option.")
            return

        if choice2 == 1:
            try:
                meters = float(input("Insert meters: "))
                kilometers = meters / 1000
                print(f"{meters:.1f} m is {kilometers:.1f} km")
            except ValueError:
                print("Input error.")

        elif choice2 == 2:
            try:
                kilometers = float(input("Insert kilometers: "))
                meters = kilometers * 1000
                print(f"{kilometers:.1f} km is {meters:.1f} m")
            except ValueError:
                print("Input error.")
                
        elif choice2 == 0:
            print("Exiting...")
            
        else:
            print("Unknown option.")

    elif choice == 2:
        
        print("\nWeight options:")
        print("1 - Grams to pounds")
        print("2 - Pounds to grams")
        print("0 - Exit")
        
        try:
            choice2 = int(input("Your choice: "))
        except ValueError:
            print("Unknown option.")
            return

        if choice2 == 1:
            try:
                grams = float(input("Insert grams:"))
                pounds = grams * 0.00220462
                print(f"{grams:.1f} g is {pounds:.1f} lb")
            except ValueError:
                print("Input error.")
            
        elif choice2 == 2:
            try:
                pounds = float(input("Insert pounds: "))
                grams = pounds / 0.00220462
                print(f"{pounds:.1f} lb is {grams:.1f} g")
            except ValueError:
                print("Input error.")
                
        elif choice2 == 0:
            print("Exiting...")
            
        else:
            print("Unknown option.")
            

    elif choice == 3 or choice == 0:
        print("Exiting...")

    else:
        print("Unknown option.")
    
    print()
    print("Program ending.")
if __name__ == "__main__":
    main()