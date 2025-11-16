import os
from typing import Optional, List, Dict

MENU_OPTIONS = {
    1: "Read values",
    2: "Amount of values",
    3: "Calculate sum of values",
    4: "Calculate average of values",
    0: "Exit"
}


def showOptions() -> None:
    """Näyttää valikkovaihtoehdot."""
    print("Options:")
    for key, value in MENU_OPTIONS.items():
        print(f"{key} - {value}") 

def askChoice() -> Optional[int]:
    """Pyytää käyttäjän valinnan."""
    try:
        choice_str = input("Your choice:")
        
        if not choice_str.isnumeric():
            return None
            
        choice = int(choice_str)
        
        if choice in MENU_OPTIONS:
             return choice
        else:
             return None
            
    except ValueError:
        return None

def readValues(values: List[float]) -> None:
    """Lukee arvot tiedostosta ja tallentaa ne liukulukuina (float) values-listaan."""
    
    filename = input("Insert filename:")
    
    values.clear()
    
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                
                if not stripped_line:
                    continue
                
                try:
                    values.append(float(stripped_line))
                except ValueError:
                    continue 
        
        print(f"Values read successfully from \"{filename}\"")

    except IOError:
        print(f"Error: Could not read file '{filename}'.")

def calculate_amount(values: List[float]) -> None:
    """Laskee ja tulostaa arvojen määrän."""
    amount = len(values)
    print(f"Amount of values - {amount}")

def calculate_sum(values: List[float]) -> None:
    """Laskee ja tulostaa arvojen summan."""
    total_sum = sum(values)

    print(f"Sum of values - {total_sum:.1f}")

def calculate_average(values: List[float]) -> None:
    """Laskee ja tulostaa arvojen keskiarvon pyöristettynä yhteen desimaaliin."""
    amount = len(values)
    if amount == 0:
        average = 0.0
    else:
        average = sum(values) / amount
    
    print(f"Average of values -{average:.1f}")


def main() -> None:
    print("Program starting.")
    
    values_list: List[float] = []
    
    while True:
        showOptions()
        
        choice = askChoice()
        
        if choice is None:
            continue
        
        if choice == 0:
            print("Exiting program.")
            break
        
        if choice == 1:
            readValues(values_list)
        
        elif len(values_list) == 0:
            if choice != 0:
                print("Error: No values read yet. Use option 1 first.")
            continue
            
        elif choice == 2:
            calculate_amount(values_list)
            
        elif choice == 3:
            calculate_sum(values_list)
            
        elif choice == 4:
            calculate_average(values_list)

        else:
            continue
            
    print("Program ending.")

if __name__ == "__main__":
    main()