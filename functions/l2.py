
#types of Arguments:
#Default Arguments: These are arguments that have a default value assigned to them. If the caller does not provide a value for that argument, the default value is used.
def greet_with_default(name="Student"):
    print(f"Hello, {name}! Welcome to the Python course.")

#calling the function without providing an argument
greet_with_default()  # Output: Hello, Student! Welcome to the Python course.

#Keyword Arguments: These are arguments that are passed to a function by explicitly specifying the parameter name. This allows you to provide values for specific parameters without relying on their order.
def greet_with_keyword(name, course):
    print(f"Hello, {name}! Welcome to the {course} course.")

#calling the function using keyword arguments
greet_with_keyword(course="Python", name="Bob")  # Output: Hello, Bob! Welcome to the Python course.

#positional Arguments: These are arguments that are passed to a function based on their position in the function call. The order of the arguments matters, and they are assigned to parameters in the order they are provided.
def greet_with_positional(name, course):
    print(f"Hello, {name}! Welcome to the {course} course.")

#calling the function using positional arguments CASE1:
greet_with_positional("Charlie", "Python")  # Output: Hello, Charlie! Welcome to the Python course.
#calling the function using positional arguments CASE2:
greet_with_positional("Python", "Charlie")  # Output: Hello, Python! Welcome to the Charlie course.

#Arbitrary Arguments: These allow you to pass a variable number of arguments to a function. In Python, you can use the *args syntax to define a function that accepts an arbitrary number of positional arguments.
def greet_with_arbitrary(*names):
    for name in names:
        print(f"Hello, {name}! Welcome to the Python course.")

#calling the function with arbitrary arguments
greet_with_arbitrary("David", "Eve", "Frank")


#for **kwargs
def greet_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"Hello, {key}! Welcome to the {value} course.")

#calling the function with keyword arguments
greet_with_kwargs(name="Grace", course="Python")  # Output: Hello, Grace! Welcome to the Python course.