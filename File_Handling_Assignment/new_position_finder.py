import termcolor
from termcolor import colored
alphabet = "abcdefghijklmnopqrstuvwxyz"
character = input("please enter a character : ")
key = int(input(colored("enter the number from which you want to move character forward : ","blue")))
position = alphabet.find(character)
newPosition = (position + key) % 26
newCharacter = alphabet[newPosition]
print("The new Character is " , newCharacter)