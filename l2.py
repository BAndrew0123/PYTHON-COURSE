#in this lesson we are going to learn about numbers in python and how to use them in our programs.
#there are three types of numbers in python: integers, floating point numbers, and complex numbers.

integer = 10
floating_point = 10.5
complex_number = 3 + 4j

print("Integer:", integer)
print("Floating Point:", floating_point)
print("Complex Number:", complex_number)

#operators can be used to perform mathematical operations on numbers. Some common operators include +, -, *, /, and %.
print("Addition:", integer + floating_point)
print("Subtraction:", integer - floating_point)
print("Multiplication:", integer * floating_point)
print("Division:", integer / floating_point)
print("Modulus:", integer % floating_point)


#comparison operators can be used to compare numbers. Some common comparison operators include ==, !=, >, <, >=, and <=.
print("Equal to:", integer == floating_point)
print("Not equal to:", integer != floating_point)
print("Greater than:", integer > floating_point)
print("Less than:", integer < floating_point)
print("Greater than or equal to:", integer >= floating_point)
print("Less than or equal to:", integer <= floating_point)

#bitwise operators can be used to perform operations on the binary representations of numbers. Some common bitwise operators include &, |, ^, ~, <<, and >>.
print("Bitwise AND:", integer & 3)
print("Bitwise OR:", integer | 3)
print("Bitwise XOR:", integer ^ 3)
print("Bitwise NOT:", ~integer)
print("Left Shift:", integer << 2)
print("Right Shift:", integer >> 2)

#membership operators can be used to check if a value is present in a sequence. Some common membership operators include in and not in.
numbers = [1, 2, 3, 4, 5]
print("Is 3 in numbers?", 3 in numbers)
print("Is 6 not in numbers?", 6 not in numbers)

#ternary operators can be used to assign a value to a variable based on a condition. The syntax for a ternary operator is: value_if_true if condition else value_if_false.
age = 18
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

