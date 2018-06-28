# # Basic Tuple example
#
# tuple_example=()
# print(tuple_example)
#
# # Two ways to create a tuple
#
# tuple_first= 'foo','bar'
# print(tuple_first)
#
# tuple_second=('foo','bar')
# print(tuple_second)
#
#Single element tuple
# tuple_example=('foo',)
# print(tuple_example)
#
# #Concatenating two tuples
#
# tuple1=(0,1,2,3)
# tuple2=('foo','bar')
# #Concatenating the above two
# print(tuple1+tuple2)
#
# #Nested tuples
# tuple1=(0,1,2,3)
# tuple2=('foo','bar')
# tuple3=(tuple1,tuple2)
# print(tuple3)
#
# #Tuple with repetition
# tuple_rep=('yello',)*3
# print(tuple_rep)
#
# #Immutable tuples
# tuple_immutable=(0,1,2,3)
# tuple_immutable[0]=4
# print(tuple_immutable)

#Slicing in tuples [start:end:step]
# tuple_slice=(0,1,2,3)
# print(tuple_slice[:])
# print(tuple_slice[1:])
# print(tuple_slice[2:4])
# print(tuple_slice[::-1])
# print(tuple_slice[::3])

#Tuple deletion example
# tuple_del=(0,1,2)
# del tuple_del
# print(tuple_del)

#Tuple length
# tuple_len=("foo","bar")
# print(len(tuple_len))

#Converting list into tuple
# list=[0,1,3]
# print(tuple(list))
# print(tuple("hello"))

# Python program to demonstrate the use of cmp() method

# # when a<b
# a = 1
# b = 2
# print(cmp(a, b))
#
# # when a = b
# a = 2
# b = 2
# print(cmp(a, b))
#
# # when a>b
# a = 3
# b = 2
# print(cmp(a, b))


#max and min functions
# print(max(80, 100, 1000))
# print(min(-20, 100, 400,-30))

#Sets two ways to initialize


# num_set={0,1,2}
# print(num_set)
# #
# num_set=set()
# print(num_set)
# #
# num_set=set([0,1,2,3,4])
# print(num_set)

#add and update functions
# color_set=set()
# #adds a single member
# color_set.add("Red")
# print(color_set)
# #adds multiple items
# color_set.update(["Blue","Green"])
# print(color_set)


#pop,remove,discard functions
# s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(s.pop())
# print(s)

# s.remove(4)
# print(s)
# print(s.remove(100))

# s.discard(5)
# print(s)
# print(s.discard(100))

#Intersection of two sets
# setx=set(["Red","Blue"])
# sety=set(["Blue","Yellow"])
# setz=setx & sety
# print(setz)

#Union of sets
# A = {'a', 'c', 'd'}
# B = {'c', 'd', 2 }
# C= {1, 2, 3}
#
# print('A U B =', A.union(B))
# print('B U C =', B.union(C))
# D=A|B
# print(D)
# D=B|C
# print(D)

#Set difference
# setx=set(["Red","Blue"])
# sety=set(["Blue","Yellow"])
# setz=setx&sety
# print(setz)
# setz=setx-setz
# print(setz)

#issubset and issuperset
# setx=set(["Red","Blue","Yellow"])
# sety=set(["Blue","Yellow"])
# issubset=setx <= sety
# print(issubset)
# issuperset=setx >= sety
# print(issuperset)

#Dictionary

dict1={'Name':'Astor','Age':12,'Class':'First'}
# print(dict1)
# print(dict1['Name'])
# print(dict1['Age'])
# print(dict1['Class'])
# #
# print(dict1['Bob'])

#Updating the dictionary

# dict1['Age']=17
# dict1['School']='DPS R.K.P'
# print(dict1)

#Deleting dict items
# del dict1['Age']
# print(dict1)
# dict1.clear()
# print(dict1)
# del dict1
# print(dict1)

#Properties of dictionary keys
#1 Ideally shouldn't put duplicate dictionary keys in case of duplicates the last value takes precedence

# dict1['Name']='Casper'
# print(dict1)

#2 Keys must be immutable which means you must use strings,numbers and tuples

# dict_key_immutable={['Name']:'Alice','Age':12}
# print(dict_key_immutable)





























