name = ''

while not name:
    print('Enter your name')
    name = input()

print('How many students will you have?')
number_students = int(input())
if number_students:
    print('Be sure to have enough chairs')
print('Done')