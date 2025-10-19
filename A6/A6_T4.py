def main_function():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    
    file_name = input("Insert filename:").strip()
    
    name_list = []
    
    print(f"Reading file '{file_name}'.")

    try:
        with open(file_name, 'r') as file:
            for line in file:
                name = line.strip() 
                
                if name: 
                    name_list.append(name)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        print("Program ending.")
        return None

    if not name_list:
        print("Analysis failed: No names found or file was empty.")
        print("Program ending.")
        return None

    print("Analysing names...")
    print("#### REPORT BEGIN ####")
    
    total_names = len(name_list)
    total_chars = 0
    shortest_len = float('inf')
    longest_len = 0
    
    for name in name_list:
        name_len = len(name)
        total_chars += name_len
        
        if name_len < shortest_len:
            shortest_len = name_len
            
        if name_len > longest_len:
            longest_len = name_len
            
    average_length = total_chars / total_names
    
    print(f"Name count: {total_names}")
    print(f"Shortest name: {shortest_len} chars")
    print(f"Longest name: {longest_len} chars")
    
    print("Average name length: {:.2f} chars".format(average_length))
    
    print("#### REPORT END ####")
        
    print("Program ending.")
    return None

main_function()