import sys

from A10_D10.txt import readValues, displayValues

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:

    n = len(PValues)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            swap_needed = False
            
            if PAsc:
                if PValues[j] > PValues[j+1]:
                    swap_needed = True
            else:
                if PValues[j] < PValues[j+1]:
                    swap_needed = True
            
            if swap_needed:
                PValues[j], PValues[j+1] = PValues[j+1], PValues[j]

    return None

def main():
    Values = []
    Filename = ""
    
    print("Program starting.")
    
    if len(sys.argv) == 2:
        Filename = sys.argv[1]
        print("The filename '{}' was passed via CLI.".format(Filename))
    else:
        Filename = input("Insert filename: ")

    readValues(Filename, Values)
    
    print("Raw '{}'->".format(Filename), end='')
    displayValues(Values, Horisontally=True)
    
    bubbleSort(Values, PAsc=True)
    print("Ascending '{}'->".format(Filename), end='')
    displayValues(Values, True)
    
    bubbleSort(Values, PAsc=False)
    print("Descending '{}'->".format(Filename), end='')
    displayValues(Values, True)
    
    print("Program ending.")
    Values.clear()
    return None

if __name__ == "__main__":
    main()