import random

def guessAge():
    guess = random.randint(15,30)
    ansr = input(f"are you {guess} years old? (y/n):")
    if ansr == 'n':
        print("RATS!")
        guessAge()
    elif ansr == 'y':
        return guess
    else: 
        print("that is an invaild input, valid inputs are lowercase y and a lowercase n!")
        guessAge()
    
    
def start():
    print("Hello I am going to guess you age")
    usrName = input("first what is your name:")
    guess = guessAge()
    print( f"{usrName} is {guess} years old.")
    playAgain = input("would you like to play again(y/n): ")
    if playAgain == 'y':
        start()
    elif playAgain == 'n':
        quit
    else:
        print("that is an invaild input, valid inputs are lowercase y and a lowercase n!")
        print("your connection will be terminated for your incorrect input")
        quit

start()