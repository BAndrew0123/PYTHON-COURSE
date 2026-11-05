#LOCAL VS GLOBAL VARIABLES
#Global variable - scope is throughout the entire program
course_name = "Python"  # This is a global variable
def print_course_name():
    #Local variable - scope is limited to inside the function it is defined in
    course_name = "Java"  # This is a local variable
    print(f"Inside the function: {course_name}")  # Output: Inside the function: Java
print_course_name()
print(f"Outside the function: {course_name}")  # Output: Outside the function: Python


#modifying global variables inside a function
#To modify a global variable inside a function, we can use the global keyword. This tells Python that we want to use the global variable instead of creating a new local variable with the same name
count = 0  # This is a global variable
def increment_count():
    global count  # Declare that we want to use the global variable 'count'
    count += 1  # Modify the global variable
    print(f"Inside the function: {count}")  # Output: Inside the function: 1
increment_count()
print(f"Outside the function: {count}")  # Output: Outside the function: 1