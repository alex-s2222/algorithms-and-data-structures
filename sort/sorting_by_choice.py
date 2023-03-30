from random import randint
from typing import List
from testing_dec import testing

@testing
def selection_sort(array: List):
    new_array = []
    array = array.copy()

    for i in range(len(array)):
        smallest = array.index(min(array))
        new_array.append(array.pop(smallest))
    return new_array
    

if __name__ == '__main__':
    selection_sort()