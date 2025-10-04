print("Program starting.")
print()
word = "start"
word_count = 0
char_count = 0

while word != "":
    
    word = input("Insert word (empty stops): ")
    
    if word != "":
        word_count += 1
        char_count += len(word)
        
print("\nYou inserted:")
print(f"- {word_count} words")
print(f"- {char_count} characters")
print()
print("Program ending.")