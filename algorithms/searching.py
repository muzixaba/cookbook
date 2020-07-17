
def binary_search(lst, item):
    """Uses binary search to find an item in a sorted list"""
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
            
    return None

print(binary_search([1,3,5,7,9], 3))
print(binary_search([1,3,5,7,9], -1))