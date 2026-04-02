
age = 36
txt = "My name is John, I am "
print(txt,age)

age = int(input('Enter your age: '))

if age < 18:
    print('age cannot be less than 18')
elif age > 120:
    print('age cannot be greater than 120')
else:
    print('your age is:', age)

def getValid():
    while True:
        age = input('Enter your age: ')
        if age.isdigit():
            age = int(age)
            if age < 18:
                print('age cannot be less than 18')
            elif age > 120:
                print('age cannot be greater than 120')
            else:
                print('your age is:', age)
                break
        else:
            print('Please enter a numeric value')
getValid()

# Core validation Techniques
# Type checking:

# checking for an int:

value = input('enter a value: ')
if isinstance(value, int): # checks the variable
    print('An integer')
else:
    print('not an integer')
print('your value is:', value)

# range checking.Check the score is within (0-100):

score = input('enter score: ')
if isinstance(score, (float)):
    if score < 0 or score > 100:
        print('score is valid')
    else:
        print('score out of range')

print('your score is: ', score)





   