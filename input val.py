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
