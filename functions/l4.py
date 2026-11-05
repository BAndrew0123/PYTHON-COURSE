#passing arguments to a function
#pass by value:
#when we pass a value to a function, the function receives a copy of that value. Any changes made to the parameter inside the function do not affect the original value outside the function.
def modify_value(x):
    x += 5
    print(f"Inside the function: {x}")

#calling the function with a value
original_value = 10
modify_value(original_value)  # Output: Inside the function: 15
print(f"Outside the function: {original_value}")  # Output: Outside the function: 10

#pass by reference:
#when we pass a mutable object (like a list or a dictionary) to a function, the function receives a reference to that object. Any changes made to the object inside the function will affect the original object outside the function.
def modify_list(my_list):
    my_list.append(5)
    print(f"Inside the function: {my_list}")

#calling the function with a list
original_list = [1, 2, 3]
modify_list(original_list)  # Output: Inside the function: [1, 2, 3, 4]
print(f"Outside the function: {original_list}")  # Output: Outside the function: [1, 2, 3, 4]


#pass keyword: The pass statement in Python is a placeholder that does nothing when executed.
#we use it in functios,loops,conditional statements.
def greet(name, greeting="Hello"):
    pass