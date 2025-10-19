LOCATIONS = {
    0: "Home", 1: "Galba's palace", 2: "Otho's palace", 
    3: "Vitellius' palace", 4: "Vespasian's palace"
}
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PROGRESS_FILE = "player_progress.txt"

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

def read_progress() -> tuple:
    try:
        with open(PROGRESS_FILE, 'r') as f:
            lines = f.readlines()
            data_line = lines[-1].strip()
            
            parts = data_line.split(';')
            
            return int(parts[0]), int(parts[1]), parts[2]
            
    except (FileNotFoundError, IndexError, ValueError):
        return 0, 1, "01j1pvfpvcvvar"

def write_progress(current_id: int, next_id: int, passphrase: str):
    new_line = f"{current_id};{next_id};{passphrase}\n"
    
    with open(PROGRESS_FILE, 'a') as f:
        f.write(new_line)

def get_message_filename(id: int, is_ciphered: bool, passphrase: str) -> str:
    
    ext = ".gkg" if is_ciphered else ".txt"
    prefix = ""

    if is_ciphered:
        prefix = f"{id}_{passphrase}"
    else:
        prefix = f"{id}_{passphrase}_plain"
        
    return prefix + ext

def read_message(filename: str) -> str:

    try:
        with open(filename, 'r') as f:
            ciphered_message = f.read().strip() 
            
            return rot13(ciphered_message)
            
    except FileNotFoundError:
        return f"Error: Message file '{filename}' not found."
    except Exception as e:
        return f"Error reading/deciphering file: {e}"

def main():
    print("Travel starting.")
    
    current_loc, next_loc, passphrase = read_progress()

    while current_loc <= 4:
        
        current_loc_name = LOCATIONS.get(current_loc, "Unknown Location")
        next_loc_name = LOCATIONS.get(next_loc, "Unknown Location")
        
        print(f"Currently at {current_loc_name}.")
        
        if current_loc == 0:
            print(f"Walking to {next_loc_name}...")
        else:
            print(f"Arriving to {current_loc_name}...")
            print("Guards at the entrance...")
            print(f"Passphrase: \"{passphrase}\"")

            ciphered_filename = get_message_filename(current_loc, True, passphrase)
            plain_message = read_message(ciphered_filename)
            
            print("Deciphering Emperor's message...")
            print(f"Message: {plain_message}")
     
            plain_filename = get_message_filename(current_loc, False, passphrase)
            with open(plain_filename, 'w') as f:
                f.write(plain_message)
            print(f"Tools ready: Got new the plain-version-copy-of-the-Emperor's-message.")

        if next_loc > 4:
            break

        current_loc = next_loc
        next_loc += 1
        passphrase = ""

        if plain_message.startswith("Msgre:"):
             new_passphrase = plain_message.split(" ")[1]
             write_progress(current_loc, next_loc, new_passphrase)
        else:
             write_progress(current_loc, next_loc, passphrase)
             
    print("Travel ending.")

if __name__ == "__main__":
    try:
        with open(PROGRESS_FILE, 'r') as f:
            f.readline()
    except FileNotFoundError:
        with open(PROGRESS_FILE, 'w') as f:
            f.write("current_location;next_location;passphrase\n")
            f.write("0;1;01j1pvfpvcvvar\n")
            
    main()