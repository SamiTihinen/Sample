import sys
from A10_ELib import readValues, displayValues

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
 
    result = []
    i = 0
    j = 0

    while i < len(PLeft) and j < len(PRight):
        if PAsc:

            if PLeft[i] <= PRight[j]:
                result.append(PLeft[i])
                i += 1
            else:
                result.append(PRight[j])
                j += 1
        else:

            if PLeft[i] >= PRight[j]:
                result.append(PLeft[i])
                i += 1
            else:
                result.append(PRight[j])
                j += 1


    result.extend(PLeft[i:])
    result.extend(PRight[j:])


    PMerge.clear()
    PMerge.extend(result)
    return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:

    if len(PValues) <= 1:
        return None

    mid = len(PValues) // 2

    left = PValues[:mid]
    right = PValues[mid:]

    mergeSort(left, PAsc)
    mergeSort(right, PAsc)

    merge(left, right, PValues, PAsc)
    
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
    
    mergeSort(Values, PAsc=True)
    print("Ascending '{}'->".format(Filename), end='')
    displayValues(Values, True)
    
    mergeSort(Values, PAsc=False)
    print("Descending '{}'->".format(Filename), end='')
    displayValues(Values, True)
    
    print("Program ending.")
    Values.clear()
    return None

if __name__ == "__main__":
    main()