def main():
    print("Program starting.")
    
    input_str = input("Insert comma-separated integers: ")
    
    raw_values = [item.strip() for item in input_str.split(',')]
    
    valid_integers = []
    
    for value_str in raw_values:
        if not value_str:
            continue

        try:
            integer_value = int(value_str)
            valid_integers.append(integer_value)
        except ValueError:
            print(f"Error: Invalid value detected and skipped: {value_str}")
    
    count = len(valid_integers)
    
    if count == 0:
        print("No valid integers remain after parsing, inform the user that there are no values to analyze.")
    else:
        total_sum = sum(valid_integers)
        even_or_odd = "even" if total_sum % 2 == 0 else "odd"
        print(f"There are {count} integers in the list. Sum of the integers is {total_sum} and it's {even_or_odd}.")
        
    print("Program ending.")
if __name__ == "__main__":
    main()