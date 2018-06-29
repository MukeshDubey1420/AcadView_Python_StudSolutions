"""
Regular Expressions
^      Start
$      Stop
.      Any character
*      Match one character 0+ times
+      Match one character 1+ times
?      Non-greedy
\s     Whitespace
\S     Non-whitespace
[abc]  Match one character in the specified set
[^abc] Match one character not in the specified set


abc…	Letters
123…	Digits
\d	Any Digit
\D	Any Non-digit character
.	Any Character
\.	Period
[abc]	Only a, b, or c
[^abc]	Not a, b, nor c
[a-z]	Characters a to z
[0-9]	Numbers 0 to 9
\w	Any Alphanumeric character
\W	Any Non-alphanumeric character
{m}	m Repetitions
{m,n}	m to n Repetitions
*	Zero or more repetitions
+	One or more repetitions
?	Optional character
\s	Any Whitespace
\S	Any Non-whitespace character
^…$	Starts and ends
(…)	Capture Group
(a(bc))	Capture Sub-group
(.*)	Capture all
(abc|def)	Matches abc or def

"""

import re  #Importing the regex module ....

#1.

# print("Hello \n World..")
#
# print()
#
# print(r"Hello \n World..")   # r is a raw string ..eliminates any special feature of special character...

#2.
# s= "This is a test string"
# p = re.compile(r"s")    #creating PatternObject and store it in p..........
# result = p.search(s)    #searching the information (s)stored in pattern...
#
# print(result)       #Returns the object ,,,    <_sre.SRE_Match object; span=(3, 4), match='s'> is the result and tells the position of first position encountered.....

#3.
# s= "this is a test string"
# p = re.compile(r"t")    #creating PatternObject and store it in p..........
# result = p.match(s)    #searching the information (s)stored in pattern...
#
# print(result)       #Returns the object ,,,<_sre.SRE_Match object; span=(0, 1), match='t'>

#4.

# s= "This is a test string"
# p = re.compile(r"s")    #creating PatternObject and store it in p..........
# result = p.findall(s)    #searching the information (s)stored in pattern...
#
# print(result)           #Return all the patterns in form of list ...   ['s', 's', 's', 's']   occurence of word can be calculated by finding length of string....


#5.

# s= "This is a test string"
# p = re.compile(r"s")    #creating PatternObject and store it in p..........
# result = p.finditer(s)    #searching the information (s)stored in pattern...
# for r in result:
#     print(r)


#6.

# s= "This is a cat"
# p = re.sub(r"c","b",s)    #creating PatternObject and store it in p..........
# print(p)        #prints     This is a bat

#7.

