import sys
import os

def showUsage() -> None:
    """Tulostaa ohjelman synopsiksen (käyttöohjeen)."""
    print("\n[USAGE] python A9_T7.py src_file.txt dst_file.txt")
    return None

def do_copy(pSrcFile: str, pDstFile: str) -> None:
    """Suorittaa tiedoston kopioinnin try-except-lohkon sisällä."""
    try:

        with open(pSrcFile, 'r') as src:
            content = src.read()
            
        with open(pDstFile, 'w') as dst:
            dst.write(content)
            
        print(f"Copying file '{pSrcFile}' to '{pDstFile}' complete.")
        
    except FileNotFoundError:
        print(f"Error: Source file '{pSrcFile}' doesn't exist.")
        sys.exit(1)
        
    except Exception as e:
        print(f"Error during copy operation: {e}")
        sys.exit(1)
        
    return None

def main() -> None:
    print("Program starting.")
    
    if len(sys.argv) != 3:
        print("Error: Invalid amount of arguments.")
        showUsage()
        print("Program ending.")
        sys.exit(1)
        
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    
    if not os.path.exists(src_file):
        print(f"Error: Source file '{src_file}' doesn't exist.")
        print("Program ending.")
        sys.exit(1)
        
    if os.path.exists(dst_file):
        prompt = f"File '{dst_file}' already exists. Do you want to overwrite it? (Y/N):"
        overwrite = input(prompt).strip().upper()
        
        if overwrite != 'Y':
            print("Copy operation aborted by user.")
            print("Program ending.")
            sys.exit(0)
            
    do_copy(src_file, dst_file)
    
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()