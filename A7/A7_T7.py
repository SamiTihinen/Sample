import os
from typing import List, Tuple, Dict, Optional

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

CONFIGS = {
    "iconf1.txt": {
        "Rotor1": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "Rotor2": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "Rotor3": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "Reflector": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    },
    "iconf2.txt": {
        "Rotor1": "QAZWSXEDCRFVTGBYHUJNMUIKOLP",
        "Rotor2": "PLMOKNI B JHVGYTFCDRXE SWAY",
        "Rotor3": "MNBCVZXLK JHGFDSAPO I UYTR EWQ",
        "Reflector": "NOPQRSTUVWAYZABCDEFGH I J KLM"
    },
    "iconf3.txt": {
        "Rotor1": "ZSFH UYXL TKOSOP AEGN I RMWJ DV C",
        "Rotor2": "XNZJ GB L H I VUFOOP TC I AN K SWYE R",
        "Rotor3": "KPCYG RMS WLJ OFTB UVXNQZA I HED",
        "Reflector": "FVF JI AO YED KRXGCK T U Q S BMHN L"
    }
}

class Enigma:
    """Simuloi Enigma-koneen toimintaa."""

    def __init__(self):
        self.rotors: List[str] = []
        self.rotor_positions: List[int] = [0, 0, 0]
        self.reflector: str = ""
        self.plugboard: Dict[str, str] = {}

    def load_config(self, filename: str) -> bool:
        """Lataa roottorit ja heijastimen ennalta määritetystä konfiguraatiosta."""
        
        if filename not in CONFIGS:
            print(f"Error: Config file '{filename}' not found.")
            return False
        
        config_data = CONFIGS[filename]
        
        self.rotors = [
            config_data.get("Rotor1", ""),
            config_data.get("Rotor2", ""),
            config_data.get("Rotor3", "")
        ]
        
        self.reflector = config_data.get("Reflector", "")
        
        if not all(self.rotors) or not self.reflector:
            print("Error: Config file is missing rotor or reflector data.")
            return False
            
        self.rotor_positions = [0, 0, 0] 
        
        return True

    def set_plugboard(self, plugs_str: str) -> None:
        """Käsittelee plugboard-asetukset (vaadittu, mutta ei toteutettu)."""
        if not plugs_str.strip() or plugs_str.lower().strip() == 'n':
            print("No.extra.plugs.inserted.")
        else:
            print(f"Plugs inserted (ignored in this demo): {plugs_str}")

    def rotate_wheels(self) -> None:
        """
        Pyörittää roottoreita (vain ensimmäistä roottoria joka kerta).
        Tehtävänanto pyytää pyörittämään pyöriä. Yleensä Enigmassa pyörivät useammat 
        tietyissä kohdissa (notch), mutta tässä tehtävässä pyöritetään vain ensimmäistä.
        """
        self.rotor_positions[0] = (self.rotor_positions[0] + 1) % 26
        

    def encrypt_char(self, char_in: str) -> str:
        """Salakirjoittaa yhden merkin kokonaisuudessaan."""
        
        if not 'A' <= char_in <= 'Z':
            return char_in
        
        self.rotate_wheels()
        
        char_out = char_in
        
        for i in range(3):
            rotor_wire = self.rotors[i]
            rotor_pos = self.rotor_positions[i]
            
            char_index = ALPHABET.find(char_out)
            
            effective_index_in = (char_index + rotor_pos) % 26
            
            scrambled_char = rotor_wire[effective_index_in]
            
            scrambled_index = ALPHABET.find(scrambled_char)
            
            effective_index_out = (scrambled_index - rotor_pos) % 26
            
            char_out = ALPHABET[effective_index_out]
            
        char_index_before_reflector = ALPHABET.find(char_out)
        
        reflected_char = self.reflector[char_index_before_reflector]
        
        char_out = reflected_char
        
        for i in range(2, -1, -1):
            rotor_wire = self.rotors[i]
            rotor_pos = self.rotor_positions[i]
            
            char_index = ALPHABET.find(char_out)
            
            scrambled_index = rotor_wire.find(char_out)
            
            effective_index_in = (scrambled_index + rotor_pos) % 26
            
            effective_index_out = (effective_index_in - rotor_pos) % 26
            
            char_out = ALPHABET[effective_index_out]
            
        return char_out

def encrypt_row(enigma_machine: Enigma, row: str) -> str:
    """Salakirjoittaa kokonaisen rivin merkit merkeiltä."""
    
    processed_row = row.upper().replace(' ', '')
    converted_row = ""
    
    for char_in in processed_row:
        if 'A' <= char_in <= 'Z':
            
            print(f"Rotor I position: {enigma_machine.rotor_positions[0]}, "
                  f"Rotor II position: {enigma_machine.rotor_positions[1]}, "
                  f"Rotor III position: {enigma_machine.rotor_positions[2]}")
                  
            char_out = enigma_machine.encrypt_char(char_in)
            
            print(f"Character \"{char_in}\".illuminated.as.\"{char_out}\"")
            
            converted_row += char_out
        else:
            converted_row += char_in 
            
    return converted_row

def main():
    print("Program.starting.")
    enigma = Enigma()

    filename = input("Insert.config(filename): ")
    if not enigma.load_config(filename):
        print("Enigma.closing.")
        return

    plugs_str = input("Insert.plugs (y/n)?: ")
    enigma.set_plugboard(plugs_str)
    
    print("Enigma.initialized.")
    
    while True:
        enigma.rotor_positions = [0, 0, 0] 
        
        input_row = input("Insert.row (empty stops): ")
        
        if not input_row:
            break
            
        converted_row = encrypt_row(enigma, input_row)
        
        print(f"Converted.row: \"{converted_row}\"")

    print("Enigma.closing.")
    
if __name__ == "__main__":
    main()