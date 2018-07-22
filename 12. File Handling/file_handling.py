f=open('demo.txt')
# f=open('/Users/MukeshDubey/Desktop/GithubRepo/demo.txt')

f=open('demo.txt','r')
f=open('demo.txt','w')
f=open('img.bmp','r+b')

file=open('Example.txt','r')
print(file.read())
print(file.read(5))

file = open('Example.txt', 'r')
print(file.readline())
print(file.readline())

file = open('Example.txt', 'r')
print(file.readlines())

#Loop over method

file = open('Example.txt', 'r')
for line in file:
    print(line)

file = open('testfile.txt', 'w')
file.write('This is a test\n')
file.write('hello hello')

file= open('testfile.txt','w')
lines_of_text = ['One line of text here\n', 'and another line here\n', 'and yet another here\n',
                                'and so on and so forth']
file.writelines(lines_of_text)

file = open('testfile.txt', 'r')
print(file.read())
file.close()

#using with to open files

with open('first.txt') as f:
    for line in f:
        print(line)


with open('app.log','w',encoding='utf-8') as f:
    f.write('It\'s my first file\n')
    f.write('This file\n')
    f.write('contains three lines')

#Open a file
f=open('app.log','r+')
data=f.read(19)
print('Read string is:',data)

#Check current position
position=f.tell()
print('Current file position:',position)
print(f.read(10))
#
# #Repostion to the start
postion=f.seek(10,0)
data=f.read(19)
print('Again read the string: ',data)

f.close()


import os

os.rename('app.log','apple.log')

os.remove('apple.log')


with open('Example.txt', 'r') as f:
    data = f.readlines()
    print(data)
    for line in data:
        words = line.split()
        print(words)








