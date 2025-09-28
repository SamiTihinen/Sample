print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program peforms.")
print("Before the menu, please insert your name:", end=" ")
user_name = input()
print("\nOptions:")
print("1. -- Print welcome message")
print("0. -- Exit")
choice = input("Your choice:")
if choice == "1":
    print(f"Welcome {user_name}!")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")