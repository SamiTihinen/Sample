import sys
import random

random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int) -> None:

    rows = len(PMineField)
    cols = len(PMineField[0])
    
    mines_placed = 0
    while mines_placed < PMines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            mines_placed += 1
    return None

def calculateNearbys(PMineField: list[list[int]]) -> None:

    rows = len(PMineField)
    cols = len(PMineField[0])
    
    for r in range(rows):
        for c in range(cols):

            if PMineField[r][c] == 9:
                continue
            
            nearby_mines = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    
                    if i == 0 and j == 0:
                        continue
                    
                    check_r = r + i
                    check_c = c + j
                    
                    if 0 <= check_r < rows and 0 <= check_c < cols:
                        if PMineField[check_r][check_c] == 9:
                            nearby_mines += 1
            
            PMineField[r][c] = nearby_mines
            
    return None

def generateMinefield(PMineField: list[list[int]], PRows: int, PCols: int, PMines: int) -> None:

    PMineField.clear()
    
    for i in range(PRows):
        row_list = []
        for j in range(PCols):
            row_list.append(0)
        PMineField.append(row_list)
        
    layMines(PMineField, PMines)
    
    calculateNearbys(PMineField)
    
    return None

def main():
    MineField = []
    
    print("Program starting.")
    
    while True:
        print("Options:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Invalid input.")
            continue
            
        if choice == 0:
            print("Exiting program.")
            print("Program ending.")
            break
            
        elif choice == 1:
            try:
                rows = int(input("Insert rows: "))
                cols = int(input("Insert columns: "))
                mines = int(input("Insert mines: "))
                
                generateMinefield(MineField, rows, cols, mines)
            except ValueError:
                print("Invalid input numbers.")
                
        elif choice == 2:

            for row in MineField:
                print(row)
                
        elif choice == 3:
            filename = input("Insert filename: ")
            try:
                with open(filename, "w") as f:
                    for row in MineField:

                        line_str = ",".join(str(x) for x in row)
                        f.write(line_str + "\n")
            except Exception as e:
                print(f"Error saving file: {e}")
        
        else:
            print("Unknown option.")

if __name__ == "__main__":
    main()