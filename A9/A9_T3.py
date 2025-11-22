import sys

def main() -> None:
    print("Program starting.")
    
    filename = input("Insert filename:").strip()
    
    try:
        with open(filename, 'r') as file:
            
            print(f"## {filename} ##")
            print("File exists")
            print(f"## {filename} ##")
            
    except FileNotFoundError:
        print(f"Couldn't read file \"{filename}\"")
        sys.exit(1)
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
            
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()