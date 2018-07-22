count=0
while (count<9):
    print("The count is: ",count)
    count=count+1
print("Goodbye!")

for letter in "python":
    print("Current Letter: ",letter)

fruits=['banana','mango','apple']
for fruit in fruits:
    print("Current Fruit:",fruit)
print("Goodbye!")

#Printing ranges
for x in range(5):
    print(x)

for x in range(3,6):
    print(x)

for x in range(3,8,2):
    print(x)


fruits=['banana','apple','mango']
for index in range(len(fruits)):
    print("Current Fruit:",fruits[index])

#Iterating over a list

l=['geeks','for','geeks']
for i in l:
    print(i)

#Iterating over a tuple(Immutable)

t=('geeks','for','geeks')
for i in t:
    print(i)

#Iterating over a string

s="geeks"
for i in s:
    print(i)

#Iterating over dictionary

d={}
d['xyz']=123
d['abc']=345
for i in d:
    print("%s %d"%(i,d[i]))

#Nested loops- while example

i=2
while(i<100):
    j=2
    while(j<=(i/j)):
        if not (i%j):break
        j=j+1
    if(j>i/j): print(i,"is a prime number")
    i=i+1
print("Bye")

#break example

for letter in "Python":
    if letter =='h':
        break
    print("Current letter:",letter)

var =10
while var>0:
    print("Current value: ",var)
    var=var-1
    if var==5:
        break
print("Bye")

#continue example

for letter in "Python":
    if letter =='h':
        continue
    print("Current letter:",letter)

var =10
while var>0:
    print("Current value: ",var)
    var=var-1
    if var==5:
        continue
print("Bye")

#break and continue

count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break

for x in range(10):
    if x%2==0:
        continue
    print(x)

# Q-7 Hint
d={}
d['xyz']=123
d['abc']=345
#Iterating over a dictionary
for val in d.keys():
  print(val,d[val])














