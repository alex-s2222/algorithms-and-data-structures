from random import randint, choice


def create_array(len_array: int) -> list:
    array = [randint(0, 100) for i in range(len_array) ]
    return array


def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        less: list = []
        mid: list = []
        greater: list = []
        pivot = choice(array)
        
        for num in array:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                mid.append(num)

        return quick_sort(less) + mid + quick_sort(greater)


def testing() -> str:
    for i in range(20, 30):
        array = create_array(i)
        assert quick_sort(array) == sorted(array)

    return "Good"


if __name__ == '__main__':
    print(testing())


    