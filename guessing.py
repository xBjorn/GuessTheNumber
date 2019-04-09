import random
from os import system

class Guessing:
    """Creating random numbers for the guessing game"""

    def __init__(self, guess, level):
        self.guess = guess
        self.level = level


    def random_number(self, level, guess):
        """Create a random number for the user to guess"""
        
        system('CLS')
        
        #Easy difficulty
        if int(level) == 1:
            number = random.randint(1,5)
            if int(number) == int(guess):
                print("\nCongratulations! You won.")
            else:
                print("\nNice try! Better luck next time.")
                
        #Medium difficulty
        elif int(level) == 2:
            number = random.randint(1,10)
            if int(number) == int(guess):
                print("\nCongratulations! You won.")
            else:
                print("\nNice try! Better luck next time.")
                
        #Hard difficulty
        elif int(level) == 3:
            number = random.randint(1,20)
            if int(number) == int(guess):
                print("\nCongratulations! You won.")
            else:
                print("\nNice try! Better luck next time.")
                
        print("The number was: {number}".format(number=number))

   
