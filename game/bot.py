import telebot
import os
from dotenv import load_dotenv
from random import choice
import handlers.commence
import handlers.ready_checker
import handlers.game_router
import handlers.guess_hue
import handlers.guess_suit
import handlers.guess_denomination

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

GAMES = ["one", "two", "three"]
CARD_RANK = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_SUIT = ["H", "D", "S", "C"]

random_card_rank = choice(CARD_RANK)
random_card_suit = choice(CARD_SUIT)


@bot.message_handler(commands=["commence"])
def commence(message):
    bot.reply_to(message, handlers.commence.GREETING)
    bot.register_next_step_handler(message, ready_checker)


def ready_checker(message):
    user_answer = message.text.lower()

    if user_answer == "yes":
        bot.reply_to(message, handlers.ready_checker.REPLY_TO_YES)
        bot.register_next_step_handler(message, game_router)

    elif user_answer == "no":
        bot.reply_to(message, handlers.ready_checker.REPLY_TO_NO)

    else:
        bot.reply_to(message, handlers.ready_checker.REPLY_TO_UNDEFINED)
        bot.register_next_step_handler(message, ready_checker)


def game_router(message):
    game_number = message.text.lower()

    if game_number == "one":
        bot.reply_to(message, handlers.game_router.GUESS_HUE_RULES)
        bot.register_next_step_handler(message, guess_hue)

    elif game_number == "two":
        bot.reply_to(message, handlers.game_router.GUESS_SUIT_RULES)
        bot.register_next_step_handler(message, guess_suit)

    elif game_number == "three":
        bot.reply_to(message, handlers.game_router.GUESS_DENOMINATION_RULES)
        bot.register_next_step_handler(message, guess_denomination)

    else:
        bot.reply_to(message, handlers.game_router.REPLY_TO_UNDEFINED)
        bot.register_next_step_handler(message, game_router)


def guess_hue(message):
    player_answer = message.text.lower()
    if player_answer not in ["crimson", "black"]:
        bot.reply_to(message, handlers.guess_hue.UNDEFINED_ANSWER)
        bot.register_next_step_handler(message, guess_hue)
    elif player_answer == "crimson" and random_card_suit in ["H", "D"]:
        bot.reply_to(
            message,
        )
    elif player_answer == "black" and random_card_suit in ["S", "C"]:
        bot.reply_to(message, handlers.guess_hue.CORRECT_BLACK_HUE)
    else:
        bot.reply_to(message, handlers.guess_hue.WRONG_HUE)

    show_card(message)


def guess_suit(message):
    player_answer = message.text.upper()

    if player_answer not in ["H", "D", "S", "C"]:
        bot.reply_to(message, handlers.guess_suit.UNDEFINED_ANSWER)
        bot.register_next_step_handler(message, guess_suit)
    elif player_answer == random_card_suit:
        bot.reply_to(message, handlers.guess_suit.CORRECT_ANSWER)
    else:
        bot.reply_to(message, handlers.guess_suit.WRONG_ANSWER)

    show_card(message)


def guess_denomination(message):
    player_answer = message.text.upper()

    if player_answer not in CARD_RANK:
        bot.reply_to(message, handlers.guess_denomination.UNDEFINED_ANSWER)
        bot.register_next_step_handler(message, guess_denomination)
    elif player_answer == random_card_rank:
        bot.reply_to(message, handlers.guess_denomination.CORRECT_ANSWER)
    else:
        bot.reply_to(message, handlers.guess_denomination.WRONG_ANSWER)

    show_card(message)


def show_card(message):
    bot.send_message(
        message.chat.id,
        f"A card hath been conjured: {random_card_rank}{random_card_suit}",
    )


bot.infinity_polling()
