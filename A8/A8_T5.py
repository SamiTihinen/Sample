import hashlib

import os

from typing import Dict, Tuple, List, Optional



CREDENTIALS_FILE = "credentials.txt"

DELIMITER = ";"

MAIN_MENU_OPTIONS = {

    1: "Login",

    2: "Register",

    0: "Exit"

}

USER_MENU_OPTIONS = {

    1: "View profile",

    2: "Change password (no need to implement)",

    0: "Logout"

}



def _hash_password(password: str) -> str:

    """Hashaa salasanan MD5:llä ja palauttaa hexdigest-muotoisen merkkijonon."""

    return hashlib.md5(password.encode('utf-8')).hexdigest()



def _load_credentials() -> Dict[str, Tuple[int, str]]:

    """Lataa käyttäjätunnukset credentials.txt-tiedostosta muotoon {username: (user_id, hashed_password)}."""

    credentials = {}

    if not os.path.exists(CREDENTIALS_FILE):

        return credentials



    try:

        with open(CREDENTIALS_FILE, 'r', encoding='utf-8') as f:

            for line in f:

                stripped_line = line.strip()

                if not stripped_line:

                    continue

               

                parts = stripped_line.split(DELIMITER)

                if len(parts) >= 3:

                    try:

                        user_id = int(parts[0].strip())

                        username = parts[1].strip()

                        hashed_password = parts[2].strip()

                        credentials[username] = (user_id, hashed_password)

                    except ValueError:

                        continue

    except IOError:

        print(f"Error: Could not read file {CREDENTIALS_FILE}.")

   

    return credentials



def _save_credentials(credentials: Dict[str, Tuple[int, str]]) -> None:

    """Tallentaa käyttäjätunnukset credentials.txt-tiedostoon."""

    try:

        with open(CREDENTIALS_FILE, 'w', encoding='utf-8') as f:

            user_id = 0

            for username, (old_id, hashed_password) in credentials.items():

                f.write(f"{user_id}{DELIMITER}{username}{DELIMITER}{hashed_password}\n")

                user_id += 1

    except IOError:

        print(f"Error: Could not write to file {CREDENTIALS_FILE}.")



def _display_menu(menu_options: Dict[int, str]) -> None:

    """Näyttää valikkovaihtoehdot."""

    print("Options:")

    for key, value in menu_options.items():

        print(f"{key} - {value}")

def register_user(credentials: Dict[str, Tuple[int, str]]) -> bool:

    """Hoitaa uuden käyttäjän rekisteröinnin."""

    print("Insert username:")

    username = input()

    print("Insert password:")

    password = input()

   

    hashed_password = _hash_password(password)

    new_id = len(credentials)

   

    credentials[username] = (new_id, hashed_password)

   

    _save_credentials(credentials)

   

    print("User registration completed!")

    return True



def login_user(credentials: Dict[str, Tuple[int, str]]) -> Optional[Tuple[str, int]]:

    """Hoitaa sisäänkirjautumisen ja palauttaa (käyttäjänimen, user_id) onnistuessaan."""

    print("Insert.username:")

    username = input()

    print("Insert password:")

    password = input()

   

    if username not in credentials:

        print("Authentication failed!")

        return None

   

    user_id, stored_hash = credentials[username]

    hashed_input = _hash_password(password)

   

    if stored_hash == hashed_input:

        print("Authentication successful!")

        return username, user_id

    else:

        print("Authentication failed!")

        return None



def main_menu(credentials: Dict[str, Tuple[int, str]]) -> Optional[Tuple[str, int]]:

    """Käsittelee päävalikon toiminnot."""

    while True:

        _display_menu(MAIN_MENU_OPTIONS)

       

        try:

            choice = int(input("Your choice:"))

        except ValueError:

            continue

           

        if choice == 1:

            logged_in_user_data = login_user(credentials)

            if logged_in_user_data:

                return logged_in_user_data

        elif choice == 2:

            register_user(credentials)

        elif choice == 0:

            print("Exiting program.")

            return None

        else:

            continue



def user_menu(username: str, user_id: int) -> None:

    """Näyttää kirjautuneen käyttäjän valikon toiminnot."""

    print("User menu:")

    logged_out = False

    while not logged_out:

        _display_menu(USER_MENU_OPTIONS)

       

        try:

            choice = int(input("Your choice:"))

        except ValueError:

            continue

           

        if choice == 1:

            print(f"Profile ID {user_id} - {username}")

        elif choice == 2:

            print("Change password function not implemented.")

        elif choice == 0:

            print("Logging out...")

            logged_out = True

        else:

            continue



def main():

    print("Program starting.")

   

    credentials = _load_credentials()

   

    logged_in_user_data = main_menu(credentials)

   

    if logged_in_user_data:

        username, user_id = logged_in_user_data

        user_menu(username, user_id)

   

    print("Program ending.")



if __name__ == "__main__":

    main()