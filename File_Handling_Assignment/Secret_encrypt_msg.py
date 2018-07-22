alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 3

#Create a variable to store the new encrypted message.

newMessage = ""

#Entering the user message instead of single character...

Message = input("please enter a message you want to encrypt : ")

#Adding a for loop to your code, and indent the rest of the code so that it is repeated for each character in the message.
for character in Message:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition] #Test your code. You should see that each character in the message is encrypted and printed one at a time.
    # print("The new Character is ", newCharacter)
    newMessage += newCharacter  #Let’s add each encrypted character to your newMessage variable.
print("Your Encrypted code is : ",newMessage)