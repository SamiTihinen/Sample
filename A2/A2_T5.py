print("Program starting.")
print()
compound_word = input("Insert a closed compound word: ")
word_length = len(compound_word)
reversed_word = compound_word[::-1]
last_char = compound_word[-1]
print(f"The word you inserted is '{compound_word}' and in reverse it is '{reversed_word}'.")
print(f"The inserted word length is {word_length}")
print(f"Last character is '{last_char}'")
print()
print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
substring = compound_word[start:end:step]
print()
print(f"The word '{compound_word}' sliced to the defined substring is '{substring}'.")
print("Program ending.")