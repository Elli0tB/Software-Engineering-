import random

def guessAge():
    guess = random.randint(15,30)
    ansr = input(f"are you {guess} years old? (y/n):")
    if ansr != 'n' or 'y':
        print("that is invailid input, lets try again")
        guessAge()
    while ansr == 'n':
        print("RATS!")
        guessAge()
    if ansr == 'y':
        return ansr
    
    
def start():
    print("Hello I am going to guess you age")
    usrName = input("first what is your name:")
    guess = guessAge()
    print( f"{usrName}is {guess} years old.")
    quit

start()