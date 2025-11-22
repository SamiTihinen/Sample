def main() -> None:
    print("Program starting.")
    
    final_sum = 0.0
    user_input = ""
    
    while user_input != "0":
        
        prompt_text = "Insert a floating-point value (0 to stop):"
        
        user_input = input(prompt_text)
        
        if user_input == "0":
            break 
        
        try:
            value = float(user_input)

            print("{}".format(value)) 
            
            final_sum += value
            
        except ValueError:
            print(f"Error! '{user_input}' couldn't be converted to float.")
            continue
            
    print(f"Final sum is {final_sum:.2f}")
    
    print("Program ending.")

    return None

if __name__ == "__main__":
    main()