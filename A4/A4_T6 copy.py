print("Program starting.")
Feed =input("Insert a positive integer: ")
Value = int(Feed)

steps = 0

while Value !=1:
    print(Value, end=" -> ")
if Value % 2 == 0:
    Value = Value // 2
else:
    Value = 3 * Value + 1

steps += 1

print("1")
print(f"Sequence has {steps} total steps.\n")
print("Program ending.")