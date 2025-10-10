def frameword(pword):
    frame_width = len(pword) + 4
    frame_line = "*" * frame_width
    print(frame_line)
    print(f"* {pword} *")
    print(frame_line)
    return None

def main_function():
    print("Program starting.")
    print("Insert word:", end="")
    inserted_word = input()
    print()
    frameword(inserted_word)
    print()
    print("Program ending.")
    return None

main_function()