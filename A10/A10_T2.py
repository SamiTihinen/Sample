import sys
import os
from typing import List

def readValues(PFilename: str, PValues: List[int]) -> None:

    if not os.path.exists(PFilename):
        print(f"Error: File '{PFilename}' not found.")
        return

    try:
        with open(PFilename, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                
                if not stripped_line:
                    continue
                
                try:
                    value = int(stripped_line)
                    PValues.append(value)
                except ValueError:
                    continue
                    
    except IOError:
        print(f"Error: Could not read file '{PFilename}'.")
        return

    return None

def sumOfValues(PValues: List[int]) -> int:
    return sum(PValues)

def productOfValues(PValues: List[int]) -> int:
    if not PValues:
        return 0
    
    product = 1
    for val in PValues:
        product *= val
    return product

def main() -> None:
    values: List[int] = []
    
    print("Program starting.")
    
    filename = input("Insert filename: ")
    
    readValues(filename, values)
    
    if not values:

        print("Program ending.")
        return

    total_sum = sumOfValues(values)
    
    total_product = productOfValues(values)
    
    header_sum = "# --- Sum of numbers --- #"
    print(header_sum)
    print(total_sum)
    print(header_sum)
    
    header_product = "# --- Product of numbers --- #"
    print(header_product)
    print(total_product)
    print(header_product)
    
    values.clear()
    
    print("Program ending.")

if __name__ == "__main__":
    main()