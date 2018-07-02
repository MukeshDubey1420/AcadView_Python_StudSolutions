print("CHOOSE YOUR CATEGORY:\n1.FRUITS\n2.ANIMALS\n3.BOLLYWOOD MOVIE\n4.HOLLYWOOD MOVIE")
ch=int(input("ENTER CHOICE-"))
if ch==1:
    word=['k','i','w','i']
    word2=[]
    c = len(word)
    k=0
    for k in range (0,c):
        word2.append('_')
    print("\n->HINT: A green coloured fruit\n->word is-  ",end=' ')
    b = 0
    for b in range(0, c):
        b = word2[b]
        print(b, end=' ')
elif ch==2:
    word = ['l','i','z','a','r','d']
    word2 = []
    c = len(word)
    k = 0
    for k in range(0, c):
        word2.append('_')
    print("\n->HINT: A reptile\n->word is-  ",end=' ')
    b = 0
    for b in range(0, c):
        b = word2[b]
        print(b, end=' ')
elif ch==3:
    word = ['p','i','n','k']
    word2 = []
    c = len(word)
    k = 0
    for k in range(0, c):
        word2.append('_')
    print("\n->HINT: Name of a colour\n->word is-  ",end=' ')
    b = 0
    for b in range(0, c):
        b = word2[b]
        print(b, end=' ')
else:
    word = ['d','e','a','d','p','o','o','l']
    word2 = []
    c = len(word)
    k = 0
    for k in range(0, c):
        word2.append('_')
    print("\n->HINT: A Marvel superhero\n->word is-  ",end=' ')
    b = 0
    for b in range(0, c):
        b = word2[b]
        print(b, end=' ')
lives=5
w=0
print("\n->You have 5 lives")
while lives>0 and w<c:
    inp=input("\n\n->Enter your guess(enter in lowercase)-")
    y=0
    x=0
    for x in range (0,c):
        if inp==word[x]:
            y=y+1
    if y>0:
        w=w+y
        s=0
        for s in range (0,c):
            if inp==word[s]:
                word2[s]=inp
        print("->Word now:  ",end=' ')
        b=0
        for b in range (0,c):
            b=word2[b]
            print(b,end=' ')
    else:
        lives=lives-1
        print("\n!! 1 LIFE REDUCED !!\nLIVES REMAINING:-",lives)
        print("->Word now:   ",end=' ')
        b = 0
        for b in range(0, c):
            b = word2[b]
            print(b, end=' ')
if w==c:
    print("\n!! CONGRATS YOU WON !!\n--Coded by: ANSH ARORA--")
else:
    print("\n!! YOU LOST !!\n--Coded by: ANSH ARORA--")
