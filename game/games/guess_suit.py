def play(card_suit):

    print("Divine its suit.\n\n")

    player_answer = ""

    while player_answer not in ["H", "D", "S", "C"]:
        player_answer = input(
            "Thou hast but four choices at thy disposal:\n"
            '"S" is for spades,\n'
            '"D" is for diamonds,\n'
            '"H" is for hearts,\n'
            '"C" is for clubs.'
            "I seeketh but a single letter, devoid of punctuation marks.\n"
        ).upper()

    if player_answer == card_suit:
        print("Thou hast divined the suit! May thy lineage flourish!")
    else:
        print(
            "Thou hast not divined!\n"
            "The benevolent God shall cast many sorrows upon thy woeful fate!"
        )
