current_count = 0
def showOptions_function():
    print("\nOptions:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None
def askChoice_function():
    choice_str = input("Your choice: ")
    if choice_str.isnumeric():
        return int(choice_str)
    else:
        return 99
def main_function():
    global current_count
    print("Program starting.")
    choice = None
    while choice != 0:
        showOptions_function()
        choice = askChoice_function()
        if choice == 1:
            print(f"Current count: - {current_count}")
        elif choice == 2:
            current_count += 1
            print("Count increased!")
        elif choice == 3:
            current_count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option!")
    print()
    print("Program ending.")
    return None
main_function()