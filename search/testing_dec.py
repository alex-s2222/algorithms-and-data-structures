from random import randint

def __create_array(len_array: int) -> list:
    return [i for i in range(len_array)]


def testing(func):
    def wrapper():
        count = 100
        for i in range(10):
            arr = __create_array(count)
            desired_element = arr[randint(0, count-1)]

            assert func(arr, desired_element) == arr.index(desired_element)
        print('GooD')
    return wrapper 