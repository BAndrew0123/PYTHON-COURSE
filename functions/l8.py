#Lambda Functions- Lambda functions are small anonymous functions, meaning they do not have a defined name. These are small, short-lived functions used to pass simple logic to another function.


name = "Andrew Kimani"
upper = lambda a: a.upper()

print(upper(name))  # Output: ANDREW KIMANI

#USE CASES:
#1.conditions

check= lambda x:"Positive" if x>0 else "Negative" if x<0 else "Zero"

print(check(5))   # Output: Positive

#2.list comprehension(We will discuss list comprehension in detail in later sections)

mult = [lambda arg=x: arg*10 for x in range(1, 6)]
for func in mult:
    print(func())  # Output: 10, 20, 30, 40, 50

#3. Returning Multiple Result
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)