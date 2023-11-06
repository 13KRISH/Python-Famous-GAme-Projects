#          Guess The Number
# It Is a game in which computer select a number from (a to b) example from (1 to 10)
#  & we have to guess the correct number
import random
def user_guess(x):
    random_number=random.randint(1,x)
    # above line will return a number in range 1 to x
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess A Number From 1 to {x}:"))
        if guess<random_number:
            print("Sorry,guess again.Too Low")
        elif guess>random_number:
            print("Sorry,guess again.Too High")
    print(f"Yay,COngrats.You have guessed the correct number {random_number} correctly")        

user_guess(20)    