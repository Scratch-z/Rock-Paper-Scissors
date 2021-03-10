import random

name = input('Enter your name: ')
print(f'Hello, {name}')

scores_f = open('rating.txt', 'a')
scores_f.close()

scores_f = open('rating.txt', 'r')

name_list = (0, 0)

for x in scores_f:
    if name in x:
        name_list = x.split()

scores_f.close()

score = int(name_list[1])

options = (input().split(','))
if options == ['']:
    options = ['rock', 'paper', 'scissors']

print("Okay, let's start")

while True:
    action = input()
    comp_action = random.choice(options)

    if action in options:
        ind = options.index(action)
        halflen = len(options) // 2
        defeat_list = []
        for x in range((ind - halflen), ind):
            defeat_list.append(options[x])

        if comp_action == action:
            print(f'There is a draw ({comp_action})')
            score += 50
        elif comp_action not in defeat_list:
            print(f'Sorry, but the computer chose {comp_action}')
        elif comp_action in defeat_list:
            print(f'Well done. The computer chose {comp_action} and failed')
            score += 100
    elif action == '!exit':
        print('Bye!')
        quit()
    elif action == '!rating':
        print(f'Your rating: {score}')
    else:
        print('Invalid input')
