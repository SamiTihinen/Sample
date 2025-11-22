
TEMP_MIN = -273.15
TEMP_MAX = 10000.0

class RangeError(Exception):
    """Laukaistaan, kun lämpötila on sallitun alueen ulkopuolella."""
    pass

def collectCelsius() -> float:
    """Kysyy Celsius-lämpötilan ja tarkistaa sen kelpoisuuden."""
    
    feed = input("Insert Celsius:")
    
    try:
        celsius = float(feed)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{feed}'")

    if celsius < TEMP_MIN or celsius > TEMP_MAX:
        raise RangeError(f"{celsius} temperature out of range.")
        
    return celsius

def main() -> None:
    print("Program starting.")
    
    try:

        collected_temp = collectCelsius()

        print(f"You inserted: {collected_temp:.1f}°C")
        
    except ValueError as e:

        print(e)
        
    except RangeError as e:
        print(e)
        
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()