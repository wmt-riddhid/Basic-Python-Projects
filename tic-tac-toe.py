# This is a Tic-Tac-Toe game python program

# Using dictionary, we will create our game board, 'key':'value'
import math
import random

'''
from cgitb import reset
from itertools import count
from pdb import Restart
from shutil import move
'''

theboard = { '7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '
}

board_keys = []

for key in theboard:
    board_keys.append(key)

def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# now, we will write the main function, which has all gameplay functionalities

def game():
    
    turn = 'X'
    count = 0

    for i in range(10):
        printboard(theboard)
        print("It's Your turn " + turn + " . Move to which place ? ")
        
        move = input()
        
        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1
        else:
            print("Sorry ! That place is already filled.\nMove to which place ? ")
            continue

# now, we will check if the player X or 0 wins or not, for every moves after 5 moves

        if count >= 5 :
            if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                printboard(theboard)
                print("\nGAME OVER !!!\n")
                print("*****" +turn + "won. *****")
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                printboard(theboard)
                print("\nGAME OVER !!!\n")
                print("*****" +turn + "won. *****")
                break
            elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                printboard(theboard)
                print("\nGAME OVER !!!\n")
                print("*****" +turn + "won. *****")
                break
            elif theboard['7'] == theboard['4'] == theboard['1'] != ' ':
                printboard(theboard)
                print("\nGAME OVER !!!\n")
                print("*****" +turn + "won. *****")
                break
            elif theboard['8'] == theboard['5'] == theboard['2'] != ' ':
                printboard(theboard)
                print("\nGAME OVER !!!\n")
                print("*****" +turn + "won. *****")
                break
            elif theboard['9']==theboard['6']==theboard['3'] != ' ':
                printboard(theboard)
                print("\nGAME OVER !!!\n")
                print("*****" +turn + "won. *****")
                break
            elif theboard['7']==theboard['5']==theboard['3'] != ' ':
                printboard(theboard)
                print("\nGAME OVER !!!\n")
                print("*****" +turn + "won. *****")
                break
            elif theboard['9']==theboard['5']==theboard['1'] != ' ':
                printboard(theboard)
                print("\nGAME OVER !!!\n")
                print("*****" +turn + "won. *****")
                break
# if neither X wins nor 0 wins, then it will be a tie

        if count == 9:
            print("\nGAME OVER\n")
            print("It's a tie")

# now, we have to change the player after every move

        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'

# now, we will have to ask player to restart the game or not

    Restart = input("Do you want to restart the game ? (y/n) ")
    if Restart == "y" or Restart == "Y":
        for key in board_keys:
            theboard[key] = " "
        game()
if __name__ == "__main__":
    game()