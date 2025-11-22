LINES_TO_SAVE = []

def writeFile(Filename: str, Content: list) -> None:
    """Kirjoittaa listan sisällön tiedostoon ja tulostaa vahvistuksen."""
    try:
        text_content = "\n".join(Content)
        with open(Filename, 'w') as file:
            file.write(text_content)
        print("Lines saved!")
    except Exception as e:
        print(f"Error during file saving: {e}")
    return None

def saveLines(pFilename: str, pContent: list) -> None:
    """Funktio, jota testikoodi kutsuu tallennusoperaatioon."""
    writeFile(pFilename, pContent)
    return None


def print_menu() -> None:
    """Tulostaa valikon vaihtoehdot."""
    print("Options:")
    print("1. - Insert line")
    print("2. - Save lines")
    print("0. - Exit")
    return None

def handle_interrupt() -> None:
    """Käsittelee KeyboardInterrupt-syötteen ja kysyy tallennusta."""
    global LINES_TO_SAVE
    
    print("Keyboard interrupt and unsaved progress!") 
    
    if len(LINES_TO_SAVE) > 0:
        
        save_prompt = input("Save before quit (y/n)?:").strip().lower()
        
        if save_prompt == 'y':
            filename = input("Insert filename:").strip()
            if filename:
                saveLines(filename, LINES_TO_SAVE)
            else:
                print("Filename not specified. Closing program.")
        else:
            print("Program ending.")
            
    else:
        print(" Closing suddenly.") 
        print("Program ending.")

    sys.exit(0)


def main() -> None:
    global LINES_TO_SAVE
    print("Program starting.")
    
    choice = None
    
    try:
        while choice != "0":
            print_menu()
            
            user_input = input("Your choice: ")
            choice = user_input.strip()
            
            if choice == "1":
                line = input("Insert text: ").strip()
                LINES_TO_SAVE.append(line)
                
            elif choice == "2":
                if LINES_TOVE:
                    filename = input("Insert filename: ").strip()
                    if filename:
                        saveLines(filename, LINES_TO_SAVE)
                    else:
                        print("Filename not specified.")
                else:
                    print("No lines to save.")
                    
            elif choice == "0":
                print("Program ending.")
                break 
                
            else:
                print("Unknown option!")
                
    except KeyboardInterrupt:
        handle_interrupt()

    return None


if __name__ == "__main__":
    import sys
    main()