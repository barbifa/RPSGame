from random import randint

# re-import our game variables
from gameComponents import gameVars, compareFunctions, validationFunctions, graphicsFunctions

while gameVars.player_choice is False:
    print("==================*/ RPS GAME */====================")
    print("Computer Lives:", end='')
    graphicsFunctions.drawlives(gameVars.computer_lives)
    print("\nPlayer Lives:", end='')
    graphicsFunctions.drawlives(gameVars.player_lives)
    print("\n====================================================")
    print("Choose your weapon! Or type quit to exit\n") #\n means "new line"

    while not gameVars.user_input_valid:
        gameVars.player_choice = input("Choose rock, paper, or scissors: \n")
        validationFunctions.validateuserinput()

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("user chose: " + gameVars.player_choice)
    print("computer chose: " + gameVars.computer_choice)

    compareFunctions.compareusercomputerchoice()
    compareFunctions.setthewinnerloser()
    gameVars.user_input_valid = False
