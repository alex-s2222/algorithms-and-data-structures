from random import randint
from typing import List
from create_arr import create_array


def recurs_binary_search(array: List, search_element: int, low: int = None, high: int = None) -> int | None:
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1

    if low <= high:
        mid = int((low + high) / 2)
        guess = array[mid]

        if guess == search_element:
            return mid
        elif guess > search_element:
            return recurs_binary_search(array=array, search_element=search_element, low=low, high=mid-1)
        elif guess < search_element:
            return recurs_binary_search(array=array, search_element=search_element, low=mid+1, high=high)
    else:
        return None


def testing(count_testing=10) -> str:
    count = 100
    for i in range(count_testing):
        arr = create_array(count)
        desired_element = arr[randint(0, count-1)]
        assert recurs_binary_search(array=arr, search_element=desired_element) == arr.index(desired_element)
    
    return "GooD"


if __name__ == '__main__':
    print(testing())