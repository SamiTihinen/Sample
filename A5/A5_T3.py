def askName_function():
    print("Insert name:", end="")
    name = input()
    return name
def greetUser_function(pname):
    print(f"Hello, {pname}!")
    return None
def main_function():
    print("Program starting.")
    user_name = askName_function()
    greetUser_function(user_name)
    print("Program ending.")
    return None
main_function()
