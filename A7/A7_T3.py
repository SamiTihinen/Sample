import os

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def readFile(pFilename: str, pRows: list[str]) -> None:
    """
    Lukee määritetyn tiedoston rivi riviltä, ohittaa otsikkorivin ja 
    lisää kelvolliset datatrivit (ilman rivinvaihtoa) pRows-listaan.
    """
    print(f"Reading file: \"{pFilename}\".")
    
    pRows.clear() 
    
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
                
                pRows.append(stripped_line)
                
    except IOError:
        print(f"Error: Could not read file '{pFilename}'.")
        return None

    return None

def analyseTimestamps(pRows: list[str], pResults: list[str]) -> None:
    """
    Analysoi pRows-listan rivit, laskee aikaleimat viikonpäivittäin ja 
    täyttää pResults-listan muotoilluilla tuloksilla.
    """
    print("Analysing timestamps.")
    
    pResults.clear()
    
    weekdayTimestampAmount = [0] * len(WEEKDAYS)
    
    for row in pRows:
        for i, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                weekdayTimestampAmount[i] += 1
                break
    
    print("Displaying results.")
    print("## Timestamp analysis ###")
    
    for i, day in enumerate(WEEKDAYS):
        count = weekdayTimestampAmount[i]
        
        result_str = f"..{day}.{count}.stamps"
        pResults.append(result_str)
        
    print("## Timestamp analysis ###")
    return None

def displayResults(pResults: list[str]) -> None:
    """
    Iteroi pResults-listan läpi ja tulostaa tulokset.
    """

    for result_line in pResults:
        print(result_line)
    
    return None

def main():
    print("Program starting.")
    
    rows_list = []
    results_list = []

    filename = input("Insert filename: ")
    
    readFile(filename, rows_list)
    
    if rows_list:
        analyseTimestamps(rows_list, results_list)
    else:
        print("No data rows found to analyze.")

    if results_list:
        displayResults(results_list)
    elif rows_list:
        pass
    rows_list.clear()
    results_list.clear()

    print("Program ending.")

if __name__ == "__main__":
    main()