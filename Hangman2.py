import random
def hangman(choice):
    word = choice
    len = word.__len__()
    ans = ['_']*len
    l = 6
    count = 0
    print(ans)
    chosen = []
    while l > 0:
        g = input('Enter a letter: ')
        guess = g.lower()
        counter = 0
        if guess not in chosen:
            chosen.append(guess)
            for i in range(0, len):

                if guess == word[i]:
                    count += 1
                    ans[i] = guess
                    counter = 1
            print(ans)
            if len == count:
                print('Voila! You won...')
                break
            if counter == 0:
                l -= 1
                life(l)
        else:
            chosen.sort()
            print('You have already tried! -->', chosen)




def life(l):
    if l == 5:
        print('''         ______
        |
        |
        |
        |
        |      ''')
    elif l == 4:
        print('''         ______
        |      |
        |
        |
        |
        |      ''')
    elif l == 3:
        print('''         ______
        |      |
        |      O
        |     
        |      
        |      ''')
    elif l == 2:
        print('''         ______
        |      |
        |      O
        |     \|/
        |      
        |      ''')
    elif l == 1:
        print('''         ______
        |      |
        |      O
        |     \|/
        |      |
        |      ''')
    elif l == 0:
        print('''         ______
        |      |
        |      O
        |     \|/
        |      |
        |     /|\ ''')
        print('        You Lost!')


name = input('Knock Knock!! Who\'s This? ')
print("Welcome %s! \nLet's play HanGMaN..." % name)
print(''' ______
|      |
|      O
|     \|/
|      |
|     /|\ ''')
cat = int(input('What would u like to have? \n1. Movies \n2. Colors \n3. Fruits \nPick a no.:'))
movies = ['raazi', 'avtaar', 'kahaani']
colors = ['red', 'blue', 'violet']
fruits = ['orange', 'banana', 'apple']
if cat == 1:
    choice = random.choice(movies)
    print('Great Choice! You seem a Movie Geek...')
elif cat == 2:
    choice = random.choice(colors)
    print('Great Choice! Let\'s form a rainbow...')
elif cat == 3:
    choice = random.choice(fruits)
    print('Great Choice! We have a Foodie here...')
print('On your mark, Get set, Go!')
if choice == 'raazi':
    print('Clue --> Agreed ')
if choice == 'avtaar':
    print('Clue --> Versions')
if choice == 'kahaani':
    print('Clue --> Story')
if choice == 'red':
    print('Clue --> I\'m gonna kill you!!')
if choice == 'blue':
    print('Clue --> A glass of water please')
if choice == 'violet':
    print('Clue --> Voila')
if choice == 'orange':
    print('Clue --> A fruit ')
if choice == 'banana':
    print('Clue --> Oops! I slipped... ')
if choice == 'apple':
    print('Clue --> Alia Bhatt\'s Movie ')

hangman(choice)
