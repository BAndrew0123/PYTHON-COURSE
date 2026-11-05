#nested functions

def outer_function(x):
    def inner(x,y):
        return x + y
    return inner(x, 5)

output = outer_function(10)
print(output)

#return Statements: is used to end a function and send a value back to the caller.
def add_numbers(a,b):
    return a + b

result = add_numbers(3, 4)
print(result)  # Output: 7