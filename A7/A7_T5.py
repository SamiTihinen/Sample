import os
from typing import List, Dict, Optional
from dataclasses import dataclass

DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")
DATA_FILENAME_PREFIX = "A7_T5_" 

@dataclass
class TIMESTAMP:
    """Tietorakenne yhdelle aikaleimariville (raakadata)."""
    weekday: str
    hour: int
    consumption: float
    price: float

@dataclass
class DAY_USAGE:
    """Tietorakenne päivittäiselle kulutukselle ja kustannuksille."""
    total_consumption: float = 0.0
    total_cost: float = 0.0


def readTimestamps(pFilename: str, pTimestamps: List[TIMESTAMP]) -> None:
    """
    Lukee tiedoston, ohittaa otsikon, jäsentää rivit TIMESTAMP-olioiksi
    ja lisää ne pTimestamps-listaan.
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
                    continue
                
    except IOError:
        print(f"Error: Could not read file '{pFilename}'.")
        return None

    return None

def analyseAndSummarize(pTimestamps: List[TIMESTAMP], pResults: List[str]) -> None:
    """
    Analysoi aikaleimat, laskee päivittäiset kulutukset ja kustannukset, 
    ja muotoilee tulokset pResults-listaan.
    """
    print("Analysing timestamps.")
    pResults.clear()
    
    daily_usage_gatherer: List[DAY_USAGE] = [DAY_USAGE() for _ in range(len(WEEKDAYS))]
    
    for ts in pTimestamps:
        try:
            day_index = WEEKDAYS.index(ts.weekday)
        except ValueError:
            continue

        daily_usage_gatherer[day_index].total_consumption += ts.consumption

        daily_cost = ts.consumption * ts.price
        daily_usage_gatherer[day_index].total_cost += daily_cost
        
    print("Displaying results.")
    pResults.append("### Electricity consumption summary ###")

    for day_index, usage_data in enumerate(daily_usage_gatherer):
        day = WEEKDAYS[day_index]
        
        result_str = (
            f" - {day} usage {usage_data.total_consumption:.2f} kwh,"
            f" cost {usage_data.total_cost:.2f} €"
        )
        pResults.append(result_str)
        
    pResults.append("### Electricity consumption summary ###")

    return None

def displayResults(pResults: List[str]) -> None:
    """Tulostaa muotoillut tulokset."""
    for result_line in pResults:
        print(result_line)
    
    return None

def main():
    print("Program starting.")
    timestamps_list: List[TIMESTAMP] = []
    results_list: List[str] = []
 
    filename = input("Insert filename: ")
    
    readTimestamps(filename, timestamps_list)
    
    if timestamps_list:
        analyseAndSummarize(timestamps_list, results_list)
    else:
        print("No data rows found to analyze.")

    if results_list:
        displayResults(results_list)
    
    timestamps_list.clear()
    results_list.clear()

    print("Program ending.")
if __name__ == "__main__":
    main()