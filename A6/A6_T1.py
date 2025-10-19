def main_function():
    print("Program starting.")
    print("This program can read a file.")
    
    file_name = input("Insert filename:").strip() 
    
    start_line = f"#### START \"{file_name}\" ####"
    end_line = f"#### END \"{file_name}\" ####"
    
    try:
        with open(file_name, 'r') as file:
            print(start_line)
            
            file_content = file.read()
            print(file_content, end="")
            
            print(end_line)
            
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    print("Program ending.")
    return None

main_function()