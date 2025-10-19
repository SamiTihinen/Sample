def main_function():
    print("Program starting.")
    first_name = input("Insert first name:")
    last_name = input("Insert last name:")
    file_name = input("Insert filename:")

    try:
        with open(file_name, 'w') as file:
            file.write(first_name + '\n')
            file.write(last_name + '\n')

        print("Program ending.")

    except Exception as e:
        print(f"Error: An unexpected error occurred during file writing: {e}")

    return None

main_function()