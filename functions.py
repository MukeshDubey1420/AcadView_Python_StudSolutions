#Basic function definition

a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))

def sum(a,b):
    '''Docstring example'''
    sum=a+b
    return sum

print("The sum of the numbers is: ",sum(a,b))
print(sum.__doc__)

#Calling a function

def printme(str):
    print(str)
    return
printme("I'm the first call to the function")
printme("Second call to the function")

#Pass by reference vs Pass by value

def changeme(mylist):
    "This changes the list passed to the function"
    mylist.append([1,2,3,4])
    print("Values inside the function",mylist)
    return

list=[10,20,30]
changeme(list)
print("Values outside the function",list)

def changeme(mylist):
    "This changes the list passed to the function"
    mylist=[1,2,3,4]
    print("Values inside the function",mylist)
    return

mylist=[10,20,30]
changeme(mylist)
print("Values outside the function",mylist)

#Function arguments - required argument,keyword and default
def printme(str):
    "Prints the passed string to it"
    print(str)
    return

printme()

#Keyword argument
def printinfo(name,age):
    "Prints information passed to it"
    print("Name:",name)
    print("Age:",age)
    return
printinfo(age=50,name="Alice")

#Default argument
def printinfo(name,age=35):
    "Prints information passed to it"
    print("Name:",name)
    print("Age:",age)
    return
printinfo(age=50,name="Alice")
printinfo("Alice")

#Return statement example
def sum(arg1,arg2):
    total=arg1+arg2
    print("Inside the function:",total)
    return total

total=sum(10,20)
print("Outside of function:",total)

#Scope of a variable- Global and local
add=0
def sum(a,b):
    add=a+b
    print(add)
    return add
sum(10,5)
print(add)

add=0 #Global variable
def sum(a,b):
    total=a+b  #Local variable
    return total
add=sum(10,5)
print(add)
print(total)

#Recursion

def calc_factorial(x):
    if(x==1):
        return x
    else:
        return x*calc_factorial(x-1)
num=5
print("Factorial of number is:",calc_factorial(num))
















