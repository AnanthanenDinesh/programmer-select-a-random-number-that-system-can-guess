import random
def computer_guess(x):
    low = 1
    high= x
    feedback=""
    while feedback != "c":
        if low!= high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"is {guess} to high (H),too low(L), or correct(c).lower()")
        if feedback == "h":
            high = guess-1
        if feedback == "l":
            low = guess+1
    print("super your guess is correct")
computer_guess(10)
