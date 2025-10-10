def askDimension(pPrompt: str) -> float:
    print(f"Insert {pPrompt}:", end="")
    try:
        Feed = float(input())
    except ValueError:
        print("Invalid input. Please insert a valid number.")
        return 0.0
    return Feed
def calcRectangleArea(pWidth: float, pHeight: float) -> float:
    Area = pWidth * pHeight
    return Area
def main_function():
    print("Program starting.")
    Width = askDimension("width") 
    Height = askDimension("height") 
    Area = calcRectangleArea(Width, Height)
    print()
    print(f"Area is {Area:.1f}\nProgram ending.")
    
    return None

main_function()