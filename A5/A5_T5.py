current_word = ""

def print_menu():
    print("\nOptions:")
    print("1. - Insert word") 
    print("2. - Show current word")
    print("3. - Show current word in reverse")
    print("0. - Exit")

def main_function():
    global current_word
    print("Program starting.")
    choice = None
    while choice != "0":
        print_menu()
        choice = input("Your choice:")

        if choice == "1":
            print("Insert word:", end="")
            current_word = input() 
            
        elif choice == "2":
            print(f"Current word: \"{current_word}\"")

        elif choice == "3":
            if current_word:
                reversed_word = current_word[::-1]
            else:
                reversed_word = "" 
            
            print(f"Word reversed: \"{reversed_word}\"")

        elif choice == "0":
            print("Exiting program.")
        else:
            print("Unknown option.")

    print()
    print("Program ending.")
    return None

main_function()