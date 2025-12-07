import sys
import time
import copy
from typing import Callable

try:
    from A10_ELib import readValues
except ImportError:
    def readValues(filename, list_ref):
        try:
            with open(filename, 'r') as f:
                content = f.read().replace(',', ' ').split()
                for item in content:
                    list_ref.append(int(item))
        except FileNotFoundError:
            print(f"File {filename} not found.")

def bubbleSort(PValues: list[int]) -> list[int]:

    n = len(PValues)
    for i in range(n):
        for j in range(0, n - i - 1):
            if PValues[j] > PValues[j+1]:
                PValues[j], PValues[j+1] = PValues[j+1], PValues[j]
    return PValues

def quickSort(PValues: list[int]) -> list[int]:

    if len(PValues) <= 1:
        return PValues
    else:
        pivot = PValues.pop()
        greater = []
        lower = []
        for item in PValues:
            if item > pivot:
                greater.append(item)
            else:
                lower.append(item)
        return quickSort(lower) + [pivot] + quickSort(greater)


def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:

    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    ElapsedTime = EndTime - StartTime
    return ElapsedTime


def main():
    Values = []
    Results = []
    Filename = ""
    
    print("Program starting.")
    
    while True:
        print("Options:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 0:
            print("Exiting program.")
            print("Program ending.")
            break
            
        elif choice == 1:
            Values.clear()
            Filename = input("Insert dataset filename: ")
            readValues(Filename, Values)
            
        elif choice == 2:
            if not Values:
                print("No data loaded. Read dataset first.")
                continue
                
            print(f"Measured speeds for dataset '{Filename}':")
            
            data_copy = copy.deepcopy(Values)
            time_builtin = measureSortingTime(sorted, data_copy)
            res_str1 = f" - Built-in sorted {time_builtin} ns"
            print(res_str1)
            Results.append(res_str1)
            
            data_copy = copy.deepcopy(Values)
            time_bubble = measureSortingTime(bubbleSort, data_copy)
            res_str2 = f" - Bubble sort {time_bubble} ns"
            print(res_str2)
            Results.append(res_str2)
            
            data_copy = copy.deepcopy(Values)
            time_quick = measureSortingTime(quickSort, data_copy)
            res_str3 = f" - Quick sort {time_quick} ns"
            print(res_str3)
            Results.append(res_str3)
            
        elif choice == 3:
            result_filename = input("Insert results filename: ")
            try:
                with open(result_filename, "w") as f:
                    f.write(f"Measured speeds for dataset '{Filename}':\n")
                    for line in Results:
                        f.write(line + "\n")
            except Exception as e:
                print(f"Error saving file: {e}")
                
        else:
            print("Unknown option.")

    Values.clear()
    Results.clear()

if __name__ == "__main__":
    main()