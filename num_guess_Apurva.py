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
    num = random.randint(1, 100)
    print(num) # this line works
    guess = int(input("Please guess a number in the range 1-100: "))
    if num == guess:
        count = count_attempts(count)
        print(f"You got it in {count} attempts!")
    elif (guess < num) or (guess > num):
        count = count_attempts(count)
        if guess < num:
            print(f"You got it wrong, the number is larger than your guess, try again: ")
            guess_rand_num(count)
        else:
            print(f"You got it wrong, the number is smaller than your guess, try again: ")
            guess_rand_num(count)
    else:
        print(f"This is invalid")

#def generate_rand_num() -> int:
    #"""
    #doc string
    #"""
    #return random.randint(1, 100)


#def take_input() -> int:
#    """
#    doc string
#    """
#    input("Please guess a number in the range 1-100: ")

def count_attempts(i: int) -> int:
    """
    doc string
    """
    i = (i + 1)
    return i

guess_rand_num(0)
