def play(card_suit):

    print("Venture a guess upon the hue of the suit: black or crimson?")
    player_answer = ""

    while player_answer not in ["crimson", "black"]:
        player_answer = input(
            "Declare the hue and presseth enter.\n"
            "There be but two choices - black and crimson.\n"
        ).lower()

    if player_answer == "crimson" and card_suit in ["H", "D"]:
        print(
            "Huzzah! Thou hast prevailed, forsooth!\n"
            "Thou hast divined the card aright!"
        )
    elif player_answer == "black" and card_suit in ["S", "C"]:
        print("Hail and well done! Thou hast correctly divined the card!")
    else:
        print("Verily, thou hast not guessed the card!")
