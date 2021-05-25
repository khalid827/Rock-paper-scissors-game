"""
The game is called rock paper scissors
"""
import random
def main():
    round=content()
    loop_of_games=many_games(round)


def many_games(round):
    human_score=0
    computer_score=0
    tie_score=0
    for i in range(round):
        human=human_move()
        computer=computer_move()
        information(human,computer)
        logic=main_logic(human,computer)
        print("In ",i+1," round ",logic,"won")
        human_score, computer_score,tie_score=calc_score(logic,human_score,computer_score,tie_score)
    print("Human Score is",human_score)
    print()
    print("Computer Score is",computer_score)
    print()
    print("Tie Score is",tie_score)
    print()
    
def calc_score(logic,human_score,computer_score,tie_score):
    if logic=='tie':
        tie_score=tie_score+1
    if logic=='human':
        human_score=human_score+1
       # return human_score
    if logic=='computer':
        computer_score=computer_score+1
    return human_score,computer_score,tie_score

"""
The main logic is written here
"""
def main_logic(human,computer):
    if human==computer:
        return 'tie'
    if human=='rock':
        if computer=='scissors':
            return 'human'
        return 'computer'
    if human=='scissors':
        if computer=='paper':
            return 'human'
        return 'computer'
    if human=='paper':
        if computer=='rock':
            return 'human'
        return 'computer'

"""
The information whon won in round is written here
"""
def information(human,computer):
    print("Human move is ",human)
    print()
    print("Computer move is",computer)
    print()
def computer_move():
    compute_move=random.randint(1,3)
    if compute_move==1:
        return 'rock'
    if compute_move==2:
        return 'paper'
    if compute_move==3:
       return 'scissors'

"""
Human move logic 
"""
def human_move():
    while True:
        move=input("Enter your move in rock paper and scissors in all capital or all small letters only  ")
        if is_valid(move):
            return move
        print("invalid statement")
def is_valid(move):
    if move=='rock' or move=='ROCK':
        return True
    if move=='PAPER' or move=='paper':
        return True
    if move=='scissors' or move=='SCISSORS':
        return True
    return False

def content():
    print("The rules of the game are is")
    print()
    print("Rock beats scissors")
    print("Scissors beats paper")
    print("Paper beats rock")
    print()
    round=int(input("Enter how many round you want to play "))
    return round
if __name__=='__main__':
    main()