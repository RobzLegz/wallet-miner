import re
from colorama import init
from termcolor import colored
from threading import Timer
import random

from hash_chars import chars

init()

got_btc = False
chance = 10000

def generate_hash():
    fake_hash = ""

    while len(fake_hash) < 75:
        hash_char_index = random.randint(0, len(chars) - 1)
        hash_char = chars[hash_char_index]

        fake_hash = f"{fake_hash}{hash_char}"

    return fake_hash


def generate_btc_amount():
    btc_amount = "0.00"

    while len(btc_amount) < 7:
        btc_char_index = random.randint(0, 9)
        btc_amount_char = chars[btc_char_index]

        btc_amount = f"{btc_amount}{btc_amount_char}"

    return btc_amount


def print_hash():
    full_hash = generate_hash()
    is_correct = random.randint(0, chance)

    print_text = ""

    got_btc = False

    if is_correct == chance:
        btc_amount = generate_btc_amount()
        btc_string = f"({btc_amount} BTC)"

        print_text = f"{full_hash} {colored(btc_string, 'green')}"
        got_btc = True
    else:
        print_text = f"{full_hash} {colored('(0 BTC)', 'red')}"

    print(print_text)

    return got_btc

while got_btc == False:
    got_btc = print_hash()

print("\n")
print("\n")
