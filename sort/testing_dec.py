from random import randint


def __create_array(len_array: int) -> list:
    array = [randint(0, 100) for i in range(len_array) ]
    return array


def testing(func):
    def wrapper():
        for i in range(20, 100, 10):
            arr = __create_array(i)
            assert func(arr) == sorted(arr)
        print('GooD')
    return wrapper
