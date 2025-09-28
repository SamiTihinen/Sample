print ("Program starting.")
print ("Insert two integers.")
try:
    first_integer = int(input("Insert first integer: "))
    second_integer = int(input("Insert second integer: "))
except ValueError:
    print("Invalid input. Please insert valid integers.")
    exit()
print("Comparing inserted integers.")

if first_integer > second_integer:
    print("First Integer is greater.")
elif second_integer > first_integer:
    print("Second Integer is greater.")
else:
    print("Integers are the same.")
sum_of_integers = first_integer + second_integer

print(f"\nAdding integers together")
print(f"{first_integer} + {second_integer} = {sum_of_integers}")
print("\nChecking the parity of the sum...")
if sum_of_integers % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd.")
print("Program ending.")