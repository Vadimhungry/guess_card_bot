from random import choice
from games import guess_hue, guess_suit, guess_denomination


CARD_RANK = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_SUIT = ["H", "D", "S", "C"]

random_card_rank = choice(CARD_RANK)
random_card_suit = choice(CARD_SUIT)

print(
    "Greetings, fellow wayfarer!\n"
    "We shall partake in the guessing of the card.\n"
    "The stakes are high - the manor, the lives of thy offspring, "
    "and thy very honor.\n"
    "The choice of game rules is thine.\n\n"
    "Options:\n"
    "One - Guess the hue\n"
    "Two - Guess the suit\n"
    "Three - Guess the denomination\n"
)


GAMES = ["one", "two", "three"]

while True:
    game_choice = input(
        "Declare the number of the option and presseth enter:\n"
    ).lower()

    if game_choice in GAMES:
        break
    else:
        print(
            "Art thou inebriated?\n"
            "Concentrate thyself and do not befuddle the LETTERS.\n"
            "Try again, oh wayward and sorrowful wanderer.\n"
            f'There be but three options: {", ".join(GAMES)}\n'
        )

print("The choice is made.. Let the quest commence!")
print("I hath conjured a card.\n")
if game_choice == "one":
    guess_hue.play(random_card_suit)
elif game_choice == "two":
    guess_suit.play(random_card_suit)
elif game_choice == "three":
    guess_denomination.play(random_card_rank)

print(f"A card hath been conjured: {random_card_rank}{random_card_suit}")
