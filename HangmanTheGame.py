def print_no_new(string):
    import sys
    sys.stdout.write(string)
    sys.stdout.flush()
import time
import random
r="WELCOME TO HANGMAN"
for i in r:
    time.sleep(0.25)
    print_no_new(i)
lives=6
jumble=""
word="hello"
w=list(word)
n="_"
l=list(n*len(word))
time.sleep(0.1)
print("\nGuess the word ")
time.sleep(0.2)
count=0
while w:
 position = random.randrange(len(w))
 jumble+= w[position]
 w = w[:position] + w[(position + 1):]
j=list(jumble)
print(j)
print("\n",l)
while(lives>0):
    guess=input("\n Enter the guess: ")
    if guess not in word:
        hangman = ["""









        --------
        """, """

        |   
        |
        |
        |
        |
        |
        |
        |
        --------
        """, """
        -----
        |   
        |
        |
        |
        |
        |
        |
        |
        --------
        """, """
        -----
        |   |
        |   |
        |
        |
        |
        |
        |
        |
        --------
        """, """
        -----
        |   |
        |   0
        |
        |
        |
        |
        |
        |
        --------
        """, """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | | 
        |  | | 
        |
        --------
        HANGED
        """]
        print(hangman[6 - lives])
        lives=lives-1
        print ("Now lives are= ",lives)
    for i in word:
        if(guess==i):
            print (guess)
            j.remove(guess)
            l[word.index(guess)]=guess
            for p in range(word.index(guess), len(word)):
                if (word[p] == guess):
                    l[p] = guess
            print(l)
            print(j)
            count=count+1
    if count==len(word):
        win="YOU WIN "
        for i in win:
            time.sleep(0.2)
            print_no_new(i)
        break
if(lives==0):
    lose="YOU LOSE "
    for i in lose:
        time.sleep(0.2)
        print_no_new(i)

