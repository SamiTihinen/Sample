def main() -> None:
    print("Program starting.")
    
    rgb_values = []
    colors = ["red", "green", "blue"]
    error_occurred = False
    
    try:

        for color in colors:
            user_input = input(f"Insert {color}: ")
            
            try:
                value = int(user_input)
            except ValueError:

                print(f"\"{user_input}\" is non-numeric value.")
                error_occurred = True
                break
            
            if value < 0 or value > 255:
                print(f"Value \"{value}\" is out of the range 0-255.")
                error_occurred = True
                break
                
            rgb_values.append(value)
            
        if not error_occurred:
            red = rgb_values[0]
            green = rgb_values[1]
            blue = rgb_values[2]
            
            print("RGB Details:")
            print(f"- Red {red}")
            print(f"- Green {green}")
            print(f"- Blue {blue}")
            
            hex_color = f"#{red:02x}{green:02x}{blue:02x}"
            print(f"- Hex {hex_color}")
            print(f"- Bin {red:08b} {green:08b} {blue:08b}")
            
    except Exception:
 
        error_occurred = True

    if error_occurred:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()