import random
from art import tprint
import os

def game_logo():
    tprint(text='''Guess
    The 
    Number''',font='block')

def clear_screen():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def game():
    guessed_number = random.randint(1, 100)
    print(f"gussed number is : {guessed_number}\n")
    lives=1
    while True:
        level=input("Choose level 'hard' or 'easy' : " )
        if level=='hard' or level=='easy':
            break
        else:
            print("\ninvalid choice please select from the given choice !\n")
    if level == 'hard':
        print('\nyou have 5 lives.\n ')
        lives = 5
    elif level == 'easy':
        print('\nyou have 10 lives. \n')
        lives = 10
    while lives:
        user_gussed=int(input("Guess the number: "))
        if user_gussed < guessed_number:
            if guessed_number-user_gussed>3:
                print("\nToo low\n")
            else:
                print("\nyou're close , little higher!\n")
        elif user_gussed > guessed_number:
            if user_gussed-guessed_number>3:
                print("\nToo high\n")
            else:
                print("\nyou're close , little lower!\n")

        elif user_gussed == guessed_number:
            tprint("\nYou win!\n")
            break
        lives-=1
        print(f"Number of lives {lives}\n")
        if lives==0:
            tprint(text="\nYou loose.")
    if input("\nYou want to play again? 'y' or 'n' : ")=='y':
        clear_screen()
        game_logo()
        game()
    else:
        print("thanks for playing ! ")
game_logo()
game()
