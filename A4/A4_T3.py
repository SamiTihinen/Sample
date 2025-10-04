print("Program starting.")
print()

try:
    start_value = int(input("Insert starting value: "))
    stopping_value = int(input("Insert stopping value: "))
except ValueError:
    print("Invalid input. Please insert valid integers.")
    exit()

current_number = start_value

print("\nStarting while-loop:")

while current_number <= stopping_value:
    
    if current_number < stopping_value:
        print(current_number, end=".")
    else:
        print(current_number)

    current_number += 1
print()
print("Program ending.")