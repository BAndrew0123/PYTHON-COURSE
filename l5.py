#in this lesson we will be learning about conditional statements in python and how to use them in our programs.
#there are three types of conditional statements in python: if, elif, and else.

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

#nested elif
student_age = 19
is_student = True


if student_age > 18:
    if is_student:
        print("You can get the book.")

else:
    print("You cannot get the book.")

#conditional expressions, also known as ternary operators, can be used to assign a value to a variable based on a condition. The syntax for a conditional expression is:
# value_if_true if condition else value_if_false.

age =10
print("adult") if age >= 18 else print("minor")


#Match-Case Statement
#Match-Case statement is used to compare a value against multiple patterns and execute the matching block of code

day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

