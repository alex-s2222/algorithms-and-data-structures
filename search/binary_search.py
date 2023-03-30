from random import randint
from create_arr import create_array
from testing_dec import testing


@testing    # для чистоты кода 
def binary_search(arr, search_element):
    """что массив должен быть отсортирован в порядка возрастания"""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high)/2)
        guess = arr[mid]

        if guess == search_element:
            return mid
        elif guess > search_element:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    binary_search()


