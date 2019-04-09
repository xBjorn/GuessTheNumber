from guessing import Guessing
from os import system

def run_game():
    greeting = "\n\nWelcome to Bjorn's Guessing Game\n"+"="*30
    asking_string = "\nPick a difficulty level:\n1: Easy(1,5)\n2: Medium(1,10)\n3: Hard(1,20)\n\n"
    print(greeting)
    level = input(asking_string)
    system('CLS')
    levels = {'1':5,'2':10,'3':20}  
    
    
    
    
      
    #Error handling
    if level not in levels.keys():
        print("Try again")
    else:
        if int(level) == 1:
            print("\nYou picked [Easy difficulty]\nPick a number between 1 and 5\n")
        elif int(level) == 2:
            print("\nYou picked [Medium difficulty]\nPick a number between 1 and 10\n")
        elif int(level) == 3:
            print("\nYou picked [Hard difficulty]\nPick a number between 1 and 20\n")
        
        guess = input()
        
        
        #if len(guess) == 0 or int(guess) > levels[int(level)] or type(guess) == str:
        if int(guess) > levels[level]:
            system('CLS')
            print("Try again")
            
            
        else:
            gs = Guessing(guess,level)
            gs.random_number(level,guess)




run_game()
