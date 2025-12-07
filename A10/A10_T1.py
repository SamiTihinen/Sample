import os

def main():
    print("Program starting.")
    
    filename = input("Insert filename: ")
    
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        print("Program ending.")
        return

    lines = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                
                if stripped:
                    lines.append(stripped)
                    
    except Exception:
        print(f"Error: Could not read file '{filename}' ")
        print("Program ending.")
        return

    vertical_header = "# -- Vertically -- #"
    print(vertical_header)
    for item in lines:
        print(item)
    print(vertical_header)

    horizontal_header = "# -- Horizontally -- #"
    print(horizontal_header)
    
    print(", ".join(lines))
    
    print(horizontal_header)

    print("Program ending.")
if __name__ == "__main__":
    main()