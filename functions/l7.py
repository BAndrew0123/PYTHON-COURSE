#in this lesson we are going to learn about first class functions as used in python. In python functions are first class citizens which means that they can be passed as arguments to other functions, returned as values from other functions, and assigned to variables.
#1. ASSIGNING FUNCTIONS TO VARIABLES:
def msg(name):
    return f"Hello, {name}!"

# Assigning the function to a variable
f = msg

# Calling the function using the variable
print(f("Emma"))
#2. PASSING FUNCTIONS AS ARGUMENTS:
def msg(name):
    return f"Hello, {name}!"

def fun1(fun2, name):
    return fun2(name)

# Passing the msg function as an argument
print(fun1(msg, "Alex"))

#3. RETURNING FUNCTIONS FROM OTHER FUNCTIONS:
def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    return inner_function

# Calling the outer function and storing the returned inner function
inner_func = outer_function()
# Calling the inner function
print(inner_func())

#4. Storing Functions in Data Structures
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
print(d["add"](5, 3))       
print(d["subtract"](5, 3))


#HOT TAKE! - Higher order functions are functions that can take other functions as arguments or return them as results.