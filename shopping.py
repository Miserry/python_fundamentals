#1.
budget = int(input())

command = input()
while command != 'End':
    price = int(command)
    budget -= price
    if budget < 0:
        print('You went in overdraft!')
        break
    command = input()

else:
    print('You bought everything you needed.')



#2.
# budget = int(input())
#
# while budget > 0:
#     finish = input()
#     if finish != 'End':
#         finish = int(finish)
#         budget -= finish
#     else:
#         print('You bought everything you needed.')
#
#
# print('You went in overdraft!')


