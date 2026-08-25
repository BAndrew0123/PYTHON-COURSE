#in this lesson we will learn about the basic data types in python.
#there are several basic data types in python, including strings, lists, tuples, sets, and dictionaries. Each data type has its own unique characteristics and methods for manipulating data.
#1.Numeric Data Types
#1.1.Integers
#1.2.Floats
#1.3.Complex Numbers

#2.Sequence Data Types
#2.1.Strings
    #Strings are used to store text data
s = 'Welcome to the Geeks World'
print(s)
print(type(s))

# access string with index
print(s[15:20])

#2.2.Lists 
#Lists are ordered and mutable collections used to store multiple items in a single variable. 
# Elements in a list can be of different data types and are accessed using indexing.
l = [1, 2, 3, 4, 'age']
print(l)
print(type(l))

#2.3.Tuples
#Tuples are ordered and immutable collections used to store multiple items in a single variable.
# Elements in a tuple can be of different data types and are accessed using indexing.
t = (1, 2, 3, 4, 5,'age')
print(t)
print(type(t))

#3.Boolean Data Type
#Boolean values are either True or False.
b = True
print(b)
print(type(b))

#4.Set Data Type
#Sets are unordered collections of unique elements. They are mutable and can be used to perform mathematical set operations like union, intersection, and difference. Since sets are unordered, elements cannot be accessed using indexing. Elements are usually accessed by iterating through the set using a loop.
s = {1, 2, 3, 4, 5}
print(s)
print(type(s))

for i in s:
    print(i)


#5. DICT data type:are used to store data in key:value pairs.Each key in a dictionary must be unique and values are accessed using their keys with square brackets [] or get() method
d = {1: 'John', 2: 'age:20', 3: 'Doe'}
print(d[1])    
print(d.get(2))