print("Program starting.")
print()
try:
    start_value = int(input("Insert starting value: "))
    stopping_value = int(input("Insert stopping value: "))
except ValueError:
    print("Invalid input. Please insert valid integers.")
    exit()

print("\nStarting for-loop:")

for number in range(start_value, stopping_value + 1):
    print(number)

print("\nProgram ending.")
