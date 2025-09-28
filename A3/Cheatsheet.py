# A3_T3.py - Oikea korjaus:

# ... (alkuvalmistelut) ...
print("Before the menu, please insert your name:")

# TÄMÄ ON KORJATTU OSAA:
print("Name:", end=" ")
user_name = input() 
# Tässä tapauksessa 'John' on käyttäjän syöte, ja se ilmestyy 'Name:' -tekstin jälkeen.

# ... (valikon tulostaminen ja valintojen käsittely) ...