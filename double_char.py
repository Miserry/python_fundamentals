#Hello there! My goal is to ignore the loop, when the string has uppercases later with no white space.
#What am i missing?

string = input()
while string != 'End':
    for inn in string:
        if string == string.title():
            print(inn + inn, end='')
    print()
    string = input()



