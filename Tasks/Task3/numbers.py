integers = []
# get an integer from the user three times and store all of those integers in a list:
for i in range(3):
    integers.append(int(input('Enter a number: ')))

# print sum of all integers
# print the first number minus the second number
# print the third number multiplied by the first number
# print the sum of all three numbers divided by the third number
print(sum(integers))
print(integers[0]-integers[1])
print(integers[2]*integers[0])
print(sum(integers)/integers[2])
