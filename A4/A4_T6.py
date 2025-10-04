print("Program starting.")
try:
    number = int(input("Insert a positive integer: "))
    if number <= 0:
        print("Invalid input. Please insert a positive integer (> 0).")
        exit()
except ValueError:
    print("Invalid input. Please insert a valid integer.")
    exit()

current_number = number
step_count = 0
output_sequence = ""

while current_number != 1:
    
    if current_number % 2 == 0:
        current_number = current_number / 2
    else:
        current_number = (current_number * 3) + 1
        
    step_count += 1
    output_sequence += f"->{int(current_number)}"

print(f"{number}{output_sequence}")
print(f"Sequence had {step_count} total steps.")
print("Program ending.")