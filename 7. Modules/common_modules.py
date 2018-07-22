import time

# using time() to display the time elapsed in seconds since epoch
print("Seconds elapsed since epoch: ",end="")
print(time.time())

print("Time calculated according to struct_time:")
print(time.gmtime())

# asctime() and ctime()

import time

#Initializing time as gmtime()

ti=time.gmtime()
print("Time calculated using asctime():",end="")
print(time.asctime(ti))

print("Time calculated using ctime():",end="")
print(time.ctime(3000))

# Date manipulations
import datetime
from datetime import date

#Minimum represented year using datetime
print("Minimum representable year:",end="")
print(datetime.MINYEAR)

print("Maximum representable year:",end="")
print(datetime.MAXYEAR)

#representing a date using date()
print("The represented date:",end="")
print(datetime.date(1997,4,1))

#present day using today()
print("Present day:",end="")
print(date.today())

# using fromtimestamp() to calculate date
print("Date calculated from seconds elapsed since epoch in argument:",end="")
print(date.fromtimestamp(3252435))

# using min for minimum representable date
print("Minimum representable date:",end="")
print(date.min)

#using max for minimum representable date
print("Maximum representable date:",end="")
print(date.max)

# Math module
import math
print(math.ceil(4))
print(math.ceil(4.5))
print(math.fabs(-3))
print(math.factorial(3))
print(math.floor(3.5))
print(math.fsum([0.14,0.1,0.1])) #Floating sum with precision
print(math.gcd(4,8))
print(math.exp(3))
print(math.log(8,2))
print(math.pow(2,3))
print(math.cos(0))
print(math.sin(0))
print(math.tan(0))
print(math.acos(0))
print(math.asin(0))
print(math.atan(0))
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)
f=math.nan
print(float("inf")-float("inf"))

# Os module
import os

print(os.name)
print(os.getcwd())

# print absolute path
print(os.path.abspath('.'))
print(os.listdir('.'))


import os
fd ='GFG.txt'
file = open(fd, 'a')
file.write('Hello')
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
# File not closed, shown in next function.
file.close()

import datetime
from datetime import date
d=date.today()
print(d)
print(d.day)

import os
print(os.environ)











