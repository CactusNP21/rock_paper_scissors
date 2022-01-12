import random

win_results = {
    'gun': {**dict.fromkeys(['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'], True)},
    'rock': {**dict.fromkeys(['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'], True)},
    'fire': {**dict.fromkeys(['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'], True)},
    'scissors': {**dict.fromkeys(['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'], True)},
    'snake': {**dict.fromkeys(['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'], True)},
    'human': {**dict.fromkeys(['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'], True)},
    'tree': {**dict.fromkeys(['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'], True)},
    'wolf': {**dict.fromkeys(['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'], True)},
    'sponge': {**dict.fromkeys(['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'], True)},
    'paper': {**dict.fromkeys(['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'], True)},
    'air': {**dict.fromkeys(['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'], True)},
    'water': {**dict.fromkeys(['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'], True)},
    'dragon': {**dict.fromkeys(['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'], True)},
    'devil': {**dict.fromkeys(['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'], True)},
    'lightning': {**dict.fromkeys(['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'], True)},
}

items = ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
         'dragon', 'devil', 'lightning']


def input_check(points, figures):
    while True:
        user = input()
        if user in figures:
            return user, True
        elif user == '!exit':
            print('Bye')
            return user, False
        elif user == '!rating':
            print(points)
            continue
        else:
            print('Invalid input')
            continue


def start():
    username = input('Enter your name: ')
    print('Hello {}'.format(username))
    figures = input("Chose patterns for game: gun, rock, fire, scissors, snake, human, tree, wolf, sponge, paper,\n "
                    "air, water, dragon, devil, lightning. Do not write for default game").split(',')
    if figures == ['']:
        figures = ['rock', 'paper', 'scissors']
    else:
        print("Okay, let's start")
    res = ''
    with open('rating.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        if username in line:
            res = line
            res = res.strip()
    if not res:
        res = 0
        return res, figures
    res = int(res[-3:])
    return res, figures


def main():
    points, figures = start()
    while True:
        user, ok = input_check(points, figures)
        if ok:
            ai = random.choice(figures)
            try:
                if win_results[user][ai]:
                    print('Well done. The computer chose {} and failed'.format(ai))
                    points += 100
                elif user == ai:
                    print('There is a draw ({})'.format(user))
                    points += 50
            except KeyError:
                if user == ai:
                    print('There is a draw ({})'.format(user))
                    points += 50
                else:
                    print('Sorry, but the computer chose {}'.format(ai))
        else:
            break


if __name__ == '__main__':
    main()
