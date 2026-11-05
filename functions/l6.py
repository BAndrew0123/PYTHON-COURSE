#Recursions - Recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem
#Example:
def countdown(n):
  if n <= 0: #base case
    print("Done!")
  else:#recursive case
    print(n)
    countdown(n - 1)

print(countdown(5))
#Deep Explanation:
#In the above example, the countdown function takes an integer n as an argument. If n is less than or equal to 0, it prints "Done!" and stops the recursion. Otherwise, it prints the current value of n and calls itself with n - 1. This continues until n reaches 0, at which point the recursion stops and "Done!" is printed.(if n<=0) is the base case that stops the recursion, and the else block is the recursive case that continues the countdown.

#Example 2:
def factorial(n):
    if n == 0: #base case
        return 1
    else:#recursive case
        return n * factorial(n - 1)

print(factorial(5))

#Fibonacci Sequence:
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
#recursion in lists:
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))