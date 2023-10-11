import random
import os
from data import data
from art import logo, vs


def clear():
    os.system('clear')


def get_random_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_start = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_start:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_account_followers = account_a["follower_count"]
        b_account_followers = account_b["follower_count"]
        correct = check_answer(guess, a_account_followers, b_account_followers)
        clear()

        print(logo)
        if correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_start = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
