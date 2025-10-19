def main_function():
    print("Program starting.")
    print("This program can copy a file.")
    source_file = input("Insert source filename:")
    destination_file = input("Insert destination filename:")

    try:
        with open (source_file, 'r') as file:
            print(f"Reading file '{source_file}'.")

            file_content = file.read()
            print("File content ready in memory.")
        with open (destination_file, 'w') as file:
            print(f"Writing content into file '{destination_file}'.")
            file.write(file_content)
            print("Copying operation complete.")

    except Exception as e:
            print(f"Error: An unexpected error occured: {e}")

    print("Program ending.")
    return None

main_function()
