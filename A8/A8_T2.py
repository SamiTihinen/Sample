from typing import Optional, Dict


def add(pAddend1: float, pAddend2: float) -> float:
    """Suorittaa yhteenlaskun."""
    return pAddend1 + pAddend2

def subtract(pMinuend: float, pSubtrahend: float) -> float:
    """Suorittaa vähennyslaskun."""
    return pMinuend - pSubtrahend

def multiply(pMultiplicant: float, pMultiplier: float) -> float:
    """Suorittaa kertolaskun."""
    return pMultiplicant * pMultiplier

def divide(pDividend: float, pDivisor: float) -> Optional[float]:
    """Suorittaa jakolaskun. Palauttaa None, jos jaetaan nollalla."""
    if pDivisor == 0.0:
        return None
    return pDividend / pDivisor

MENU_OPTIONS = {
    1: "Add",
    2: "Subtract",
    3: "Multiply",
    4: "Divide",
    0: "Exit"
}

def showOptions() -> None:
    """Näyttää käytettävissä olevat valikkovaihtoehdot."""
    print("Options:")
    for key, value in MENU_OPTIONS.items():

        print(f"{key} - {value}")
    
def askChoice() -> Optional[int]:
    """Pyytää käyttäjän valinnan."""
    try:

        choice_str = input("Your choice:")
        
        if not choice_str.isnumeric():

            return -1 
            
        choice = int(choice_str)
        
        if choice in MENU_OPTIONS:
             return choice
        else:
 
             return -1
            
    except ValueError:
        return -1 

def askValue(pPrompt: str) -> Optional[float]:
    """Kysyy arvoa annetulla kehotteella ja palauttaa liukuluvun."""
    try:

        value_str = input(pPrompt)
        return float(value_str)
    except ValueError:
        return None

def main() -> None:
    print("Program starting.")
    
    while True:
        showOptions()
        
        choice = askChoice()
        
        if choice == -1:
            continue 
        
        if choice == 0:

            print("Exiting program.")
            break
        

        
        result = None 
        
        if choice == 1:
  
            addend1 = askValue("Insert first addend value:")
            addend2 = askValue("Insert second addend value:")
            
            if addend1 is not None and addend2 is not None:
                result = add(addend1, addend2)

                print(f"{addend1:.1f}.+.{addend2:.1f} = {result:.1f}")
            
        elif choice == 2:

            minuend = askValue("Insert minuend value:")
            subtrahend = askValue("Insert subtrahend value:")
            
            if minuend is not None and subtrahend is not None:
                result = subtract(minuend, subtrahend)
                print(f"{minuend:.1f} - {subtrahend:.1f} = {result:.1f}")
                
        elif choice == 3:

            multiplicand = askValue("Insert multiplicand value:")
            multiplier = askValue("Insert multiplier value:")
            
            if multiplicand is not None and multiplier is not None:
                result = multiply(multiplicand, multiplier)

                print(f"{multiplicand:.1f} * {multiplier:.1f} = {result:.1f}")
            
        elif choice == 4:
    
            dividend = askValue("Insert dividend value:")
            divisor = askValue("Insert divisor value:")
            
            if dividend is not None and divisor is not None:
                result = divide(dividend, divisor)
                
                if result is None:

                    print("Error: Cannot divide by zero.")
                else:
                    # Tulostus: 6.0./.3.0.=.2.0
                    print(f"{dividend:.1f} / {divisor:.1f} = {result:.1f}")
        
    print("Program ending.")


if __name__ == "__main__":
    main()