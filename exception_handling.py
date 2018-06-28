#Basic Example
while True:
    try:
        x=int(input("Enter an integer:"))
        break
    except ValueError:
        print("That was not a valid int! Try again")


#Try except else
import sys

print(sys.argv)
try:
    f=open(sys.argv[1],'r')
except OSError:
    print("Cannot open",sys.argv[1])
else:
    print(sys.argv[1],'has',len(f.readline()),'lines')
    f.close()

#Try except finally

try:
    fh=open("testfile","w")
    try:
        fh.write("This is my test file for exception handling")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Can\'t find file or read data")

#raise
import sys
def read_c():
    try:
        c=float(sys.argv[1])
    except IndexError:
        raise IndexError('Celsius degrees must be applied to command line')
    except ValueError:
        raise ValueError('Celsius degree must be a pure number,'\
                         'not "%s"'%sys.argv[1])
    #Read correctly but wrong value i.e. out of range
    if c<-273.15:
        raise ValueError('Not a physical value of Celsius')

    return c

c=read_c()

#User defined exception class

# class Error(Exception):
#     '''Base class for other exceptions'''
#     pass
# class ValueTooSmallError(Error):
#     '''Raised when the input is too small'''
#     pass
# class ValueTooBigError(Error):
#     '''Raised when the input is too large'''
#     pass
#
# #User guesses a number until they guess the right one
# number=10
# while True:
#     try:
#         i_num=int(input("Enter a number"))
#         if i_num < number:
#             raise ValueTooSmallError
#         elif i_num > number:
#             raise  ValueTooBigError
#         break
#     except ValueTooSmallError:
#         print("The value is too small, try again")
#     except ValueTooBigError:
#         print("The value is too big, try again")
# print("Congratulations! You guessed is correct")



