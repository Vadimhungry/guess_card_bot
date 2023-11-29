def play(card_rank):
    print("Divine the denomination!\n")
    print(
        "Possible options:\n"
        "Numbers from 2 to 10 is for numbers.\n"
        '"J" is for Jack.\n'
        '"Q" is for Queen.\n'
        '"K" is for King\n'
        '"A" is for Ace\n'
    )
    player_answer = input(
        "Declare the denomination of the card and presseth enter.\n"
        "Thou hast but a solitary attempt.\n"
    ).upper()

    if player_answer == card_rank:
        print(
            "Fortune smiles upon thee, thou fortunate son of a wench! "
            "All is correct!"
        )
    else:
        print("Nay! Thou art mistaken! 'Tis a curse for thy sins!")
