print("Program starting.")
print()
try:
    start_point = int(input("Insert starting point: "))
    stopping_point = int(input("Insert stopping point: "))
    inspection_point = int(input("Insert inspection point: "))
except ValueError:
    print("Invalid input. Please insert valid integers.")
    exit()

rules_broken = False

if start_point >= stopping_point:
    print("Starting point value must be less than the stopping point value.")
    rules_broken = True

if not (start_point <= inspection_point < stopping_point):
    print("Inspection point value must be within the range of start and stop.")
    rules_broken = True

if rules_broken:
    print("Program ending.")
    exit()
    

print("\nFirst loop -- inspection with break:")
output = ""
for i in range(start_point, stopping_point):
    if i == inspection_point:
        break
    
    output += str(i)
    output += ":"

if output.endswith(":"):
    output = output[:-1]

print(output)

print("Second loop -- inspection with continue:")
output = ""
for i in range(start_point, stopping_point):
    
    if i == inspection_point:
        continue
    
    output += str(i)
    output += ":"

if output.endswith(":"):
    output = output[:-1]
print(output)
print("Program ending.")