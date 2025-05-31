from random import shuffle
mylist=[' ', 'O', ' ']
def shuffle_cups(cups):
    shuffle(cups)
    return cups
def guess_cup():
    guess = ' '
    while guess not in ['1', '2', '3']:
        guess = input("Guess which cup has the ball (1, 2, or 3): ")

    return int(guess)
def check_guess(cups, guess):
    if cups[guess] == 'O':
        print("Congratulations! You found the ball!")
    else:
        print("Sorry, the ball is not under that cup.")
        print(f"The ball was under cup {mylist}.")


shuffle_cups = shuffle_cups(mylist)
user_guess = guess_cup()
check_guess(shuffle_cups,user_guess)