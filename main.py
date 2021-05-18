import random

# RPS -- Rock, Paper or Scissor


moves = ['Rock', 'Paper', 'Scissor']


def getMove():
    randomInt = random.randint(1, 3)
    move = moves[randomInt]

    return move


def getUserMove():
    move = 'j'
    while move.upper() not in moves:
        move = input("Make your choice: [R]ock, [P]aper o [S]cissor\n")

    move = move.upper()

    return move


def core(move, userMove):

    # CPU - Rock
    if move == moves[0]:
        if userMove == moves[0]:
            print('empate')
        elif userMove == moves[1]:
            print(f'you win - {userMove} defeats {move}')
        else:
            print(f'you lose - {move} defeats {userMove}')
    # CPU - Paper
    elif move == moves[1]:
        if userMove == moves[0]:
            print(f'you lose - {move} defeats {userMove}')
        elif userMove == moves[1]:
            print('empate')
        else:
            print(f'you win - {userMove} defeats {move}')
    # CPU - Scissor
    else:
        if userMove == moves[0]:
            print(f'you win - {userMove} defeats {move}')
        elif userMove == moves[1]:
            print(f'you lose - {move} defeats {userMove}')
        else:
            print('empate')


core(getMove(), getUserMove())
