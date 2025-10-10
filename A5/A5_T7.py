DELIMITER = "," 
def collectWords_function():
    word_string = ""
    word = "initial"
    while word != "":
        print("Insert word(empty stops):", end="")
        word = input()
        if word != "":
            if word_string != "":
                word_string += DELIMITER
            word_string += word
    return word_string
def analyseWords_function(pWordString):
    print() 
    word_list = pWordString.split(DELIMITER)
    word_count = len(word_list)
    char_count = 0
    for word in word_list:
        char_count += len(word)
    if word_count > 0:
        average_length = char_count / word_count
    else:
        average_length = 0.0
        
    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {0:.2f} Average word length".format(average_length))
    return None
def main_function():
    print("Program starting.")
    collected_words = collectWords_function()
    if collected_words:
        analyseWords_function(collected_words)
    
    print("Program ending.")
    
    return None
main_function()