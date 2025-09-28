print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

choice = int(input("Your choice: "))

if(choice == 1):
 
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    
    choice2 = int(input("Your choice: "))
    

    if choice2 == 1:
    
            meters = float(input("Insert meters: "))
            kilometers = meters / 1000
            print(f"{meters:.1f}m is {kilometers:.1f} km")

    elif choice2 == 2:
       
            kilometers = float(input("Insert kilometers: "))
            meters = kilometers * 1000
            print(f"{kilometers:.1f}km is {meters:.1f}m")
            
    elif choice2 == 0:
        print("Exiting...")
        
    else:
        print("Unknown option.")

elif choice == 2:
    
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    
    choice2 = int(input("Your choice: "))

    if choice2 == 1:
      
            grams = float(input("Insert grams: "))
            pounds = grams * 0.00220462
            print(f"{grams:.1f}g is {pounds:.1f}lb")
    
            
    elif choice2 == 2:
    
            pounds = float(input("Insert pounds: "))
            grams = pounds / 0.00220462
            print(f"{pounds:.1f}lb is {grams:.1f}g")
            
    elif choice2 == 0:
        print("Exiting...")
        
    else:
        print("Unknown option.")

elif choice == 0:
    print("Exiting...")

print("Program ending.")