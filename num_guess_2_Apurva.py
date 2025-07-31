import random


def guess_rand_num(count: int) -> str:
    """
    This program generates a random number and asks the user to guess it and counts their attempts

    int -> str

    count: int = keeps track of the number of attempts made by the user

    Examples:
    guess_rand_num(0) -> "You got it in 1 attempts!"
    guess_rand_num(0) -> "You got it wrong, the number is larger than your guess, try again: ",
    "You got it in 2 attempts!"
    """
    num = generate_rand_num()
    guess = take_input()
    if num == guess:
        count = count_attempts(count)
        print(f"You got it in {count} attempts!")
    elif (guess < num) or (guess > num):
        count = count_attempts(count)
        print(f"You got it in {count} attempts!")
    elif (guess < num) or (guess > num):
        count = count_attempts(count)
        if guess < num:
            print(f"You got it wrong, the number is larger than your guess, try again: {int(input())}")
        else:
            print(f"You got it wrong, the number is smaller than your guess, try again: {int(input())}")
    else:
        print(f"This is invalid")


def generate_rand_num() -> int:
    """
    this function generates a random number between 1 and 100
    """
    return random.randint(1, 100)


def take_input() -> int:
    """
    this function takes input from the user and converts it to an interger
    """
    return int(input("Please guess a number in the range 1-100: "))


def count_attempts(i: int) -> int:
    """
    this function increments the counter by 1
    """
    i = (i + 1)
    return i

guess_rand_num(0)
