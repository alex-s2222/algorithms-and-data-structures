from testing_dec import testing
import math


@testing
def linear_search(array:list, search_element: int ):
    for element in array:
        if element == search_element:
            return element
    return None 


if __name__  == '__main__':
    linear_search()

