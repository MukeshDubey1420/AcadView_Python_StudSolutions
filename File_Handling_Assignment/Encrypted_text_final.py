"""
Notice that the space and the ! characters are all encrypted as the letter ‘c’!

To fix this, you only want to translate a character if it’s in the alphabet. To do this,

add an if statement to your code, and indent the rest of your code.

"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 3

#Create a variable to store the new encrypted message.

newMessage = ""

#Entering the user message instead of single character...

Message = input("please enter a message you want to encrypt : ")

#Adding a for loop to your code, and indent the rest of the code so that it is repeated for each character in the message.
for character in Message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]  # Test your code. You should see that each character in the message is encrypted and printed one at a time.
        # print("The new Character is ", newCharacter)
        newMessage += newCharacter  # Let’s add each encrypted character to your newMessage variable.

        """
        It would be better if your code didn’t encrypt anything not in the alphabet, but just used the original character.
        Add an else statement to your code, which just adds the original character to the encrypted message.
        """
    else:
        newMessage += character

print("Your Encrypted code is : ", newMessage)