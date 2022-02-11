# This is a rock , paper , scissors game

import random

def play() :
    user = input("Please enter your choice from any of these is 'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "It's a tie"
    # we know the win conditions are r>s, s>p, p>r
    if is_win(user, computer):
        return "WooHooo !!! Congrulations....You Won the game !!!"
    return "Ohhh, Sorry..You Lose the game, Better Luck next time"
def is_win(player, opponent):
    # It will return true if player wins
    # we know the condition i.e r>s, s>p, p>r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())