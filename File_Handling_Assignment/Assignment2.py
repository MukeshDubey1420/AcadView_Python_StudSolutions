words = open("test", "r", encoding="utf8").read().split() #read the words into a list.
print(words)
print(type(words))
uniqWords = sorted(set(words)) #remove duplicate words and sort
print(uniqWords)
print(type(uniqWords))
for word in uniqWords:
    print (words.count(word), word)