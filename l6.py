#in this lesson we will be learning about loops
#forloops,while loops and nested loops are the three types of loops in python.

fruits = {'apple', 'banana', 'cherry'}

for fruit in fruits:
    print(fruit)

counter = 0
while counter < 5:
    print(counter)
    counter += 1

person = {
    "name": 'John',
    "age": 30,
    "car": 'Toyota'
}
for key, value in person.items():
    print(key, ":", value)

#nested loops
for i in range(1,5):
    for j in range(i):
        print(j, end=' ')
    print()