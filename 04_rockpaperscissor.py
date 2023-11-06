#     Rock Paper Scissor
# import random

# def play():
#     user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
#     computer = random.choice(['r', 'p', 's'])
#     if user == computer:
#         return 'It\'s a tie'
#     # r > s, s > p, p > r
#     if is_win(user, computer):
#         return 'You won!'
#     return 'You lost!'
# def is_win(player, opponent):
#     # return true if player wins
#     # r > s, s > p, p > r
#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
#         or (player == 'p' and opponent == 'r'):
#         return True
# print(play())


# Rock Paper Scissor round Game exampel
import random

def play():
    round=int(input("Enter Number Of rounds you hvae to play:"))
    player_count,computer_count=0,0
    for i in range (1,round+1):
        print(f"Round{i}:")
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r', 'p', 's'])
        print(f"Computer Choice:{computer}")
        player,computer=is_win(user,computer)
        player_count=player_count+player
        computer_count=computer_count+computer
        print(f"Your score:{player_count},Computer Score:{computer_count}")

    if(player_count>computer_count):
         print("You Won!")
    else:
         print("You Lost!")
    


    
def is_win(player, opponent):
    
    # rock > scisssor, scissor > paper, paper > rock


    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        #    return 1 if win and zero if lost
           return 1,0
    elif (player==opponent):
           return 1,1
    else:
         return 0,1
         

    

play()