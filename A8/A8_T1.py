import time
from typing import Optional, Dict

MENU_OPTIONS = {
    1: "Set pause duration",
    2: "Activate pause",
    0: "Exit"
}


def _display_menu() -> None:
    """Näyttää valikkovaihtoehdot tasan esimerkin mukaisesti."""
    print("Options:")
    for key, value in MENU_OPTIONS.items():
        # Tulostusmuoto: 1.--.Set.pause.duration
       print(f"{key} - {value}")
    
def _get_choice() -> Optional[int]:
    """Kysyy käyttäjän valinnan."""
    try:
        choice_str = input("Your choice:")
        
        if not choice_str.isnumeric():
            print("Unknown option!")
            return None
            
        choice = int(choice_str)
        
        if choice in MENU_OPTIONS or choice == 3:
             if choice == 3:
                 return 0
             return choice
        else:
            print("Unknown option!")
            return None
            
    except ValueError:
        print("Unknown option!")
        return None

def set_duration(state: Dict) -> None:
    """Kysyy ja asettaa tauon keston (sekunteina)."""
    try:
        duration_str = input("Insert pause duration (s):")
        duration = float(duration_str)
        
        if duration < 0:
            print("Error: Duration cannot be negative.")
            return

        state['duration'] = duration
        print(f"Pause duration set to {duration} seconds.")
        
    except ValueError:
        print("Error: Invalid duration format.")

def activate_pause(state: Dict) -> None:
    """Aktivoi tauon time.sleep()-funktiolla tai ilmoittaa virheestä."""
    
    if state['duration'] is None:
        print("Pause is not set.")
        print("Set pause first.")
        return

    duration = state['duration']
    
    print(f"Pausing for {duration} seconds.")
    time.sleep(duration)
    print("Unpaused.")


def main() -> None:
    print("Program starting.")
    
    program_state = {'duration': None}
    
    while True:
        _display_menu()
        
        choice = _get_choice()
        
        if choice is None:
            continue
        
        if choice == 1:
            set_duration(program_state)
        elif choice == 2:
            activate_pause(program_state)
        elif choice == 0:
   
            print("Exiting program.")
            break
            
    print("Program ending.")

if __name__ == "__main__":
    main()