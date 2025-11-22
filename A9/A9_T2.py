import sys

def main() -> None:
    print("Program starting.")
    
    prompt = "Insert exit code (0-255):"
    exit_code_str = input(prompt)
    
    try:
        exit_code = int(exit_code_str)
        
        if 0 <= exit_code <= 255:
            if exit_code == 0:
                print("Clean exit")
            else:
                print("Error code")
                
            sys.exit(exit_code)
            
        else:
            print("Error code")
            sys.exit(1)
            
    except ValueError:
        print("Error code")
        sys.exit(1)


if __name__ == "__main__":
    main()