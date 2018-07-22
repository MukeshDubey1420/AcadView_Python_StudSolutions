import random

l = []

for n in range(10):
	l.append(random.randint(1,1000))
	
with open("test.txt",'w') as f:
	for n in l:
		f.write(n)
		f.write("\n")
		
with open('test.txt','r') as f:
	l2 = f.readlines()
	
l2.sort()

with open('test2.txt','w') as f:
	for n in l2:
		f.write(n)
		f.write("\n")