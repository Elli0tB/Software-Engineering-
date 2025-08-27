import random

def guessAge():
    guess = random.randint(15,30)
    ansr = input(f"are you {guess} years old? (y/n):")
    if ansr == 'n':
        print("RATS!")
        guessAge()
    if ansr == 'y':
        return guess
    else: 
        print("that is an invaild input, valid inputs are lowercase y and a lowercase n!")
        guessAge()
    
    
def start():
    print("Hello I am going to guess you age")
    usrName = input("first what is your name:")
    guess = guessAge()
    print( f"{usrName} is {guess} years old.")
    quit

start()