LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    if Character in Alphabets:
        index = Alphabets.find(Character)
        new_index = (index + Shift) % 26
        return Alphabets[new_index]
    else:
        return Character

def rot13(Content: str) -> str:
    ciphered_text = ""
    for char in Content:
        if char in LOWER_ALPHABET:
            ciphered_text += shiftCharacter(char, LOWER_ALPHABET)
        elif char in UPPER_ALPHABET:
            ciphered_text += shiftCharacter(char, UPPER_ALPHABET)
        else:
            ciphered_text += char
    return ciphered_text

def askRows() -> str:
    all_rows = []
    row = "start"
    
    
    print("Collecting plain text rows for ciphering.") 
    
    while row != "":
        
        print("Insert row(empty stops):", end=" ")
        row = input()
        
        if row != "":
            all_rows.append(row)
            
    return "\n".join(all_rows)

def writeFile(Filename: str, Content: str) -> None:
    try:
        with open(Filename, 'w') as file:
            file.write(Content)
            print("Ciphered text saved!") 
            
    except Exception as e:
        print(f"Error during file saving: {e}") 
        
    return None

def main() -> None:
    print("Program starting.")
    
    plain_text = askRows()
    
    
    
    ciphered_text = rot13(plain_text)
    
 
    print("#### Ciphered text ####") 
    print(ciphered_text)
    print("#### Ciphered text ####")
    
  
    
    filename = input("Insert filename to save:").strip()
    
    if filename:
        writeFile(filename, ciphered_text)
    else:
    
        print("File name not defined.")
        print("Aborting save operation.")
        
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()