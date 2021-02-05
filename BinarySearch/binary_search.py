# Time O(log N) | Space O(log N)
def binary_search(array, target):
    return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(arr, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    potential_match = arr[middle]

    if potential_match == target:
        return middle
    elif potential_match > target:
        return binary_search_helper(arr, target, left, middle - 1)
    else:
        return binary_search_helper(arr, target, middle + 1, right)


# Time O(log N) | Space O(1)
def binary_search_using_iteration(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        potential_match = arr[middle]

        if potential_match == target:
            return middle
        elif potential_match > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1
