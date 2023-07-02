import random
from config import GAME_CHOICES, RULES, scoreboard
from decorators import log_time


def get_user_choices():
    # get and validate player input, recursively
    input_user = input("Enter your choices pleas(r,p,s):")
    if not input_user in GAME_CHOICES:
        print("try again please..")
        return get_user_choices()
    return input_user

def get_system_choices():
    #choice random from GAME_CHOICES
    system = random.choice(GAME_CHOICES)
    return system

def find_winner(user, system):

    math = {user, system}
    if len(math) == 1:
        return None
    return RULES[tuple(sorted(math))]

def update_scoredboard(result):
    if result['winner_system'] == 3:
        scoreboard['user'] += 1
        msg = 'you win'

    else:
        scoreboard['system'] += 1
        msg = 'you los'

    print('#'*30)
    print("##", f"user: {scoreboard['user']} ".ljust(24), "##")
    print("##", f"system: {scoreboard['system']} ".ljust(24), "##")
    print(f"## {msg} ##".ljust(24))
    print('#'*30)




def play_one_hand():

    result = {'winner_user': 0, 'winner_system': 0}

    while result['winner_user'] < 3 and result['winner_system'] < 3:
        choice_user = get_user_choices()
        choice_system = get_system_choices()
        winner = find_winner(choice_user, choice_system)

        if winner == choice_system:
            msg = 'you win'
            result['winner_system'] += 1
        elif winner == choice_user:
            msg = 'you los'
            result['winner_user'] += 1
        else:
            msg = 'Draw'

        print(f"your choice:{choice_user}\t system choice: {choice_system}\t result {msg} ")

    update_scoredboard(result)
    again_play = input("do you want to play again ?(y/n)")
    if again_play == 'y':
        play_one_hand()

@log_time
def play():
    play_one_hand()

if __name__ == '__main__':

    play()







