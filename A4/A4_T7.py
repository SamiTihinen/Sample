print("Program starting.")
print()
print("Check multiplicative persistence.")
try:
    number_str = input("Insert an integer: ") 
    int(number_str)
except ValueError:
    print("Invalid input. Please insert a valid integer.")
    exit()

current_number = number_str
step_count = 0
full_output = ""
while len(current_number) > 1:
    step_count += 1
    multiplication_result = 1
    current_step_output = "" 
    for digit in current_number:
        digit_int = int(digit)
        multiplication_result *= digit_int
        current_step_output += f"{digit} * "
        
    current_step_output = current_step_output[:-3] 
    current_step_output += f" = {multiplication_result}"
    full_output += current_step_output + "\n"
    current_number = str(multiplication_result)
    
full_output += f"No more steps."
print(full_output, end="\n\n") 
print(f"This program took {step_count} step(s)")
print()
print("Program ending.")