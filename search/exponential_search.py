from testing_dec import testing

@testing
def exponential_search(array:list, search_element: int):
    if array[0] == search_element:
        return search_element
    index = 1 
    while index < len(array) and array[index] <= search_element:
        index = index * 2
    return binary_search(array[:min(index, len(array))], search_element)



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
    exponential_search()