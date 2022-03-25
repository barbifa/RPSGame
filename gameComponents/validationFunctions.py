# all validation functions for the game

from gameComponents import gameVars


def validateuserinput():
    if gameVars.player_choice == "quit":
        print("You chose to quit")
        exit()
    elif (gameVars.player_choice.lower() != "rock") and (gameVars.player_choice.lower() != "paper") and (gameVars.player_choice.lower() != "scissors"):
        print("Please, make a valid choice")
        gameVars.user_input_valid = False
    else:
        gameVars.user_input_valid = True



