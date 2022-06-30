
string = input()
while string != 'End':
    for inn in string:
        if string == string.title():
            print(inn + inn, end='')
    print()
    string = input()



