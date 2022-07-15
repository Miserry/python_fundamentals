"""
Only works when integers in a list are in ascending order or Sorted.
"""
def binary_search(list, target):
    first = 0                           #since binary search directly goes to the middle, we have to know these two.
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2    #// is the same as floor division

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint +1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print('Target found at index:',index)
    else:
        print('Target not found in the list')

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)