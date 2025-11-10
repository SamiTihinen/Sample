def main():

    print("Program starting.")
    print("Collect positive integers.")
    
    collected_integers = []
    
    user_input = 0 
    
    while user_input >= 0:
        try:
            input_str = input("Insert positive integer (negative stops): ")
            user_input = int(input_str)
            
            if user_input >= 0:
                collected_integers.append(user_input)
                
        except ValueError:
 
            print("Validation: Only positive integers should be collected.")
            user_input = 0
            
    print("Stopped collecting positive integers.")

    
    num_collected = len(collected_integers)
    
    if num_collected == 0:
        print("No integers were collected to display.")
    else:
        print("Displaying {} integers:".format(num_collected))
        
        for index, integer in enumerate(collected_integers):
            ordinal = index + 1
            
            print("- Index: {} => Ordinal {} => Integer {}".format(index, ordinal, integer))

    print("Program ending.")

if __name__ == "__main__":
    main()