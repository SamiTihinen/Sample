print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs, \nBefore the menu, please insert your name:", end=" ")
user_name = input()
print("\nOptions:")
print("1. -- Print welcome message")
print("2. -- Print the name backwards")
print("3. -- Print the first character")
print("4. -- Show the amount of characters in the name")
print("0. -- Exit")
choice = input("Your choice: ")
if choice == "1":
    print(f"Welcome {user_name}!")
elif choice == "2":
    name_backwards = user_name[::-1]
    print(f"Your name backwards is \"{name_backwards}\"")
elif choice == "3":
    first_char = user_name[0]
    print(f"The first character in name \"{user_name}\" is \"{first_char}\"")
elif choice == "4":
    name_length = len(user_name)
    print(f"There are {name_length} characters in the name \"{user_name}\"")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")