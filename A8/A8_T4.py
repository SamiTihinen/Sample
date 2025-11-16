import os
from datetime import datetime
from typing import Optional, List, Dict, Tuple

MONTHS: List[str] = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]
WEEKDAYS: List[str] = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

MENU_OPTIONS = {
    1: "Calculate amount of timestamps during year",
    2: "Calculate amount of timestamps during month",
    3: "Calculate amount of timestamps during weekday",
    0: "Exit"
}

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"



def readTimestamps(pFilename: str, pTimestamps: List[datetime]) -> None:
    """Lukee aikaleimat tiedostosta ja muuntaa ne datetime-olioiksi."""
    print(f"Reading file: \"{pFilename}\".")
    pTimestamps.clear()
    
    if not os.path.exists(pFilename):
        print(f"Error: File '{pFilename}' not found.")
        return

    try:
        with open(pFilename, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                
                try:
                    dt_obj = datetime.strptime(stripped_line, DATETIME_FORMAT)
                    pTimestamps.append(dt_obj)
                except ValueError:
    
                    continue 
        
    except IOError:
        print(f"Error: Could not read file '{pFilename}'.")


def calculateYear(pYear: str, pTimestamps: List[datetime]) -> int:
    """Laskee aikaleimojen määrän tiettynä vuonna."""
    count = 0
    try:
        target_year = int(pYear)
    except ValueError:
        return 0
        
    for dt in pTimestamps:
        if dt.year == target_year:
            count += 1
    return count


def calculateMonth(pMonth: str, pTimestamps: List[datetime]) -> int:
    """Laskee aikaleimojen määrän tiettynä kuukautena (esim. 'January')."""
    count = 0
    
    try:
        target_month_index = MONTHS.index(pMonth)
        target_month_num = target_month_index + 1
    except ValueError:
        return 0
        
    for dt in pTimestamps:
        if dt.month == target_month_num:
            count += 1
    return count


def calculateWeekdays(pWeekday: str, pTimestamps: List[datetime]) -> int:
    """Laskee aikaleimojen määrän tiettynä viikonpäivänä (esim. 'Monday')."""
    count = 0
    
    try:
        target_weekday_index = WEEKDAYS.index(pWeekday)
    except ValueError:
        return 0
        
    for dt in pTimestamps:
        if dt.weekday() == target_weekday_index:
            count += 1
    return count

def showOptions() -> None:
    """Näyttää valikkovaihtoehdot tasan esimerkin mukaisesti."""
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


def main() -> None:
    print("Program starting.")

    timestamps_list: List[datetime] = []
    
    filename = input("Insert filename:")
    readTimestamps(filename, timestamps_list)
    
    if not timestamps_list:
        print("Error: No timestamps loaded for analysis.")
        print("Program ending.")
        return
    
    while True:
        showOptions()
        
        choice = askChoice()
        
        if choice is None:
            continue
        
        if choice == 0:
            print("Exiting program.")
            break
        
        if choice == 1:
            target_year_str = input("Insert year:")
            count = calculateYear(target_year_str, timestamps_list)
            print(f"Amount of timestamps during year '{target_year_str}' is {count}")
            
        elif choice == 2:
            target_month = input("Insert month:")
            target_month_capitalized = target_month.strip().capitalize()
            
            count = calculateMonth(target_month_capitalized, timestamps_list)
            print(f"Amount of timestamps during month.'{target_month_capitalized}' is {count}")
            
        elif choice == 3:
            target_weekday = input("Insert weekday:")
            target_weekday_capitalized = target_weekday.strip().capitalize()
            
            count = calculateWeekdays(target_weekday_capitalized, timestamps_list)
            print(f"Amount of timestamps during weekday '{target_weekday_capitalized}' is {count}")

    print("Program ending.")
if __name__ == "__main__":
    main()