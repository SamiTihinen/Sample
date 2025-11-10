import os
from typing import List
from dataclasses import dataclass

DELIMITER = ";"
DATA_FILENAME_PREFIX = "A7_T4_" 
@dataclass
class TIMESTAMP:
    """Tietorakenne yhdelle aikaleimariville."""
    weekday: str
    hour: int
    consumption: float
    price: float
    total_cost: float = 0.0

def readTimestamps(pFilename: str, pTimestamps: List[TIMESTAMP]) -> None:
    """
    Lukee tiedoston, ohittaa otsikon, jäsentää rivit TIMESTAMP-olioiksi
    ja lisää ne pTimestamps-listaan. (Päivitetty nimi testejä varten).
    """
    print(f"Reading file \"{pFilename}\".")
    pTimestamps.clear() 
    
    if not os.path.exists(pFilename):
        print(f"Error: File not found at '{pFilename}'")
        return None

    try:
        with open(pFilename, 'r', encoding='utf-8') as file_handle:
            next(file_handle, None) 
            
            for line in file_handle:
                stripped_line = line.strip()
                
                if not stripped_line:
                    continue
                
                columns = stripped_line.split(DELIMITER)
                
                if len(columns) < 4:
                    print(f"Warning: Skipping malformed row: {stripped_line}")
                    continue
                    
                try:
                    weekday = columns[0].strip()
                    hour = int(columns[1].strip())
                    consumption = float(columns[2].strip())
                    price = float(columns[3].strip())
                    timestamp = TIMESTAMP(
                        weekday=weekday,
                        hour=hour,
                        consumption=consumption,
                        price=price
                    )
                    
                    pTimestamps.append(timestamp)
                    
                except ValueError:
                    print(f"Warning: Skipping row with invalid number format: {stripped_line}")
                
    except IOError:
        print(f"Error: Could not read file '{pFilename}'.")
        return None

    return None

def displayTimestamps(pTimestamps: List[TIMESTAMP]) -> None:
    """
    Analysoi aikaleimat, laskee total_cost ja tulostaa ne. (Päivitetty nimi testejä varten).
    """
    print("Electricity.usage:")
    
    for ts in pTimestamps:
        ts.total_cost = ts.consumption * ts.price
        hour_str = f"{ts.hour:02}:00" 
        output_line = (
            f" - {ts.weekday} {hour_str}, price {ts.price:.2f}, "
            f"consumption {ts.consumption:.2f} kwh, total {ts.total_cost:.2f} €"
        )
        print(output_line)
    
    return None

def main():
    print("Program.starting.")
    
    timestamps_list: List[TIMESTAMP] = []
    filename = input("Insert.filename: ")
    readTimestamps(filename, timestamps_list)
    if timestamps_list:
        displayTimestamps(timestamps_list)
    else:
        print("No valid timestamps found to analyze.")
    timestamps_list.clear()

    print("Program.ending.")
if __name__ == "__main__":
    main()