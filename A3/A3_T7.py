print("Program starting.")
print("Testing decision structures.")

try:
    initial_value = int(input("Insert an integer: "))
except ValueError:
    print("Invalid input. Please insert a valid integer.")
    exit()

print("\nOptions:")
print("1. -- In one multi-branched decision")
print("2. -- In multiple independent if-statements")
print("0. -- Exit")

choice = input("Your choice: ")


if choice == "1":
    
    current_value = initial_value
    
    print("\nUsing one multi-branched decision structure.")


    if current_value >= 400:
        current_value += 44
    elif current_value >= 200:
        current_value += 22
    elif current_value >= 100:
        current_value += 11
        
    print(f"Result is: {current_value}")

elif choice == "2":
    
    current_value = initial_value 
    
    print("\nUsing independent if-statements.")

    
    if current_value >= 400:
        current_value += 44

    if current_value >= 200:
        current_value += 22


    if current_value >= 100:
        current_value += 11
        
    print(f"Result is: {current_value}")
    
elif choice == "0":
    print("Exiting...")
    
else:
    print("Unknown option.")
print("Program ending.")