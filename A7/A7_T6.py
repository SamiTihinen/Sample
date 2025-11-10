import random

random.seed(1234)

RPS_OPTIONS = {
    1: "rock",
    2: "paper",
    3: "scissors"
}
BOT_NAME = "RPS-3PO"
DIVIDER = "#########################" * 2

ASCII_ART = {
    "rock": (
        "...",
        ".___.",
        " / /  )",
        " / /   ",
        " -----  "
    ),
    "paper": (
        "........",
        "._______.",
        "|       |",
        "|_______|"
    ),
    "scissors": (
        "-----",
        " (_____) ",
        " (____) ",
        "  (__)  ",
        "  \\_/"
    )
}

def get_bot_choice():
    """Arpoo botin valinnan (1=rock, 2=paper, 3=scissors) random.randint(1, 3) -funktiolla."""
    bot_num = random.randint(1, 3)
    return RPS_OPTIONS[bot_num]

def check_winner(player_choice: str, bot_choice: str, player_name: str) -> str:
    """
    Tarkistaa RPS-sääntöjen perusteella voittajan.
    Palauttaa tulosviestin: "Draw", "<Player> wins" tai "<Bot> wins"
    """
    if player_choice == bot_choice:
        return f"Draw! Both players chose {player_choice}."
    
    if (player_choice == "rock" and bot_choice == "scissors") or \
       (player_choice == "paper" and bot_choice == "rock") or \
       (player_choice == "scissors" and bot_choice == "paper"):
        reason = ""
        if player_choice == "rock": reason = "rock beats scissors"
        elif player_choice == "paper": reason = "paper beats rock"
        elif player_choice == "scissors": reason = "scissors beat paper"
        
        print(f"{player_name}.{reason}.")
        return "Player wins"
    else:
        reason = ""
        if bot_choice == "rock": reason = "rock beats scissors"
        elif bot_choice == "paper": reason = "paper beats rock"
        elif bot_choice == "scissors": reason = "scissors beat paper"
        
        print(f"{BOT_NAME}.{reason}.{player_name}.{player_choice}.")
        return "Bot wins"

def print_menu():
    """Tulostaa pelin valikkovaihtoehdot."""
    print("Options:")
    for key, value in RPS_OPTIONS.items():
        print(f" {key}.--.{value.capitalize()}")
    print(" 0.--.Quit game")
    
def print_choices_and_art(player_name: str, player_choice: str, bot_choice: str):
    """Näyttää valinnat ja ASCII-taiteen erotinmerkkien kera."""
    
    print(DIVIDER)
    print(f"{player_name}.chose.{player_choice}.")
    for line in ASCII_ART.get(player_choice, []):
        print(line)
    
    print(DIVIDER)
    
    print(f"{BOT_NAME}.chose.{bot_choice}.")
    for line in ASCII_ART.get(bot_choice, []):
        print(line)
    
    print(DIVIDER)


def main():
    print("Program starting.")
    print("Welcome.to.the.rock-paper-scissors.game!")

    player_wins = 0
    bot_wins = 0
    draws = 0
    game_running = True
    
    player_name = input("Insert.player.name: ")
    print(f"Welcome.{player_name}!")
    print(f"Your.opponent.is.{BOT_NAME}.")
    print("Game.starts...")

    while game_running:
        print_menu()
        
        try:
            choice_str = input("Your.choice:")
            player_choice_num = int(choice_str)
        except ValueError:
            continue

        if player_choice_num == 0:
            game_running = False
            continue

        if player_choice_num in RPS_OPTIONS:
            player_choice = RPS_OPTIONS[player_choice_num]
            bot_choice = get_bot_choice()
            
            print("Rock!.Paper!.Scissors!.Shoot!")
            
            print_choices_and_art(player_name, player_choice, bot_choice)
            
            result = check_winner(player_choice, bot_choice, player_name)
            
            if result == "Player wins":
                player_wins += 1
            elif result == "Bot wins":
                bot_wins += 1
            else:
                draws += 1
                print(result)
            
    print("Results:")
    
    print(f"{player_name}.wins.({player_wins}).,losses.({bot_wins}).,draws.({draws})")
    
    print(f"{BOT_NAME}.wins.({bot_wins}).,losses.({player_wins}).,draws.({draws})")

    print("Program.ending.")

if __name__ == "__main__":
    main()