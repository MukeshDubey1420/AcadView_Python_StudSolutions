f = open("excerpt.txt") 
last = f.readlines()
f.close()
n = input("Enter number of last lines to be read: ")
c = n
print "The last lines are: "
while c > 0:
    print last[-c]
    c-=1
