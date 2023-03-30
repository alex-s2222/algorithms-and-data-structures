from random import randint
from typing import List


def selection_sort(array: List):
    new_array = []
    for i in range(len(array)):
        smallest = array.index(min(array))
        new_array.append(array.pop(smallest))
    return new_array


def main():
    end_rand_element = 26
    mass = [randint(0, end_rand_element) for i in range(end_rand_element)]

    print("Old array: ", mass)
    new_mass = selection_sort(mass)
    print("New array: ", new_mass)


if __name__ == '__main__':
    main()