def recursiveFactorial(PNum: int) -> int:
 
    if PNum <= 1:
        return 1
    
    return PNum * recursiveFactorial(PNum - 1)

def main():
    print("Program starting.")
    
    user_input = input("Insert factorial: ")
    
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input.")
        print("Program ending.")
        return

    print("Factorial {}!".format(number))
    
    result = recursiveFactorial(number)
    
    print("{}! = {}".format(number, result))
    
    print("Program ending.")

if __name__ == "__main__":
    main()