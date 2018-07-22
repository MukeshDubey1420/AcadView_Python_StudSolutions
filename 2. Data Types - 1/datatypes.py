#Different numerical datatypes
print(type(5))

print(type(5.0))
#
c=2+3j
print(type(c))
#
print(c+3)
#
print(isinstance(c,complex))

#Strings and str functions
var1 ="Hello World!"
var2 ="Python Programming"

print(var1[0])
print(var1[1])

print(var2[1:4])

#String methods
#len()
simple_string="Hello Hello"
print(len(simple_string))

print(simple_string+" there")
#
pi=3.14
text="The value of pi"+ str(pi)
print(text)

text="  The value of pi  "+ str(pi)
print(text)
#lower() , upper()
print(text.lower())
print(text.upper())
print(text.strip())
print(text.isalpha())

alphabet="hello"
dummy="888"
number=u"5"

print(alphabet.isalpha())
print(dummy.isdigit())
print(number.isnumeric())

dummy="Hey there you're a rockstar"
print(dummy.startswith("Hey"))
print(dummy.endswith("rockstar"))

print(dummy.find("there"))
print(dummy.find("yello"))

print(dummy.replace("Hey","Hello"))
print(dummy)

# Immutable example
dummy="hello"
dummy[0]="l"
print(dummy)

dummy="Hey,there"
print(dummy.split(','))

dummy="Yello yello"
print("!".join(dummy))

print(",".join(["red","yellow","blue"]))

#Slicing
dummy="Hello"
print(dummy[1:4])
print(dummy[1:])
print(dummy[:])
print(dummy[1:100])

print(dummy[-1])
print(dummy[-4])
print(dummy[:-3])
print(dummy[-3:])

fruits =["apple","banana","orange"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[-1])
#
mix= [1,3.0,"HELLO"]
print(mix, type(mix))
print(mix[0], type(mix[0]))
print(mix[1], type(mix[1]))
#
print(mix[100])

# #Nested List
n_list=["Yello",[2,4,6,8]]
#Nested indexing
print(n_list[0][1])
print(n_list[1][3])

#Modifyinfg list elements
fruits =["apple","banana","orange","pear"]
fruits[0]="pineapple"
print(fruits)
print(fruits[1:3])
print(fruits[:3])
print(fruits[-1])
print(fruits[:])
#
#List functions
fruits.append("mango")
print(fruits)

fruits.insert(0,"plum")
print(fruits)
#
vegetables=["potato","onion","brinjal"]
fruits.extend(vegetables)
print(fruits)

print(fruits.index("potato"))

fruits.remove("apple")
fruits.remove("banana")
print(fruits)

fruits.sort()
print(fruits)
numberlist=[500,2,5,23,1]
numberlist.sort()
print(numberlist)


fruits.reverse()
print(fruits)

fruits.pop(0)
print(fruits)

fruits.append("orange")
print(fruits)
print(fruits.count("orange"))
print(fruits.index("orange",1))







