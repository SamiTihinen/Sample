FILE_SEPARATOR = "," 
OUTPUT_SEPARATOR = ";" 

def readValues_function(pFilename: str) -> str:
    all_values = "" 
    
    try:
        with open(pFilename, 'r') as file:
            file.readline()
            
            data_line = file.readline().strip()
            
            if data_line:
                all_values = data_line 
                
    except FileNotFoundError:
        return ""
    except Exception:
        return ""

    return all_values

def analyseNumbers_function(pNumberString: str) -> tuple:
    total_sum = 0
    count = 0
    greatest = -float('inf') 
    

    number_list = [int(n) for n in pNumberString.split(FILE_SEPARATOR)]
    
    count = len(number_list)
    
    for number in number_list:
        total_sum += number
        if number > greatest:
            greatest = number
            
    if count > 0:
        average = total_sum / count
    else:
        average = 0.0
        

    return (total_sum, count, greatest, average)


def main_function():
    print("Program starting.")
    
    filename = input("Insert filename:").strip()
    
    data_string = readValues_function(filename)
    
    if not data_string:
        print("File reading failed or file was empty.")
        print("Program ending.")
        return None
        
    Count, Sum, Greatest, Average = analyseNumbers_function(data_string)
    
    print("#### NUMBER ANALYSIS - START ####")
    
    print(f"File: \"{filename}\".results:")

    header_line = f"Count{OUTPUT_SEPARATOR}Sum{OUTPUT_SEPARATOR}Greatest{OUTPUT_SEPARATOR}Average"
    print(header_line)

    value_line = (
        f"{Count}{OUTPUT_SEPARATOR}"
        f"{Sum}{OUTPUT_SEPARATOR}"
        f"{Greatest}{OUTPUT_SEPARATOR}"
        f"{Average:.2f}"
    )
    print(value_line)
    
    print("#### NUMBER ANALYSIS - END ####")

    print("Program ending.")
    return None

main_function()