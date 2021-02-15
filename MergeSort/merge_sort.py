# Time O(n log n) | Space O(n log n)

def merge_sort(array):
    if len(array) == 1:
        return array

    middle_index = len(array) // 2
    left_half = array[:middle_index]
    right_half = array[middle_index:]
    return merge_arrays(merge_sort(left_half), merge_sort(right_half))


def merge_arrays(left_half, right_half):
    sorted_array = [None] * (len(left_half) + len(right_half))
    k = i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array[k] = left_half[i]
            i += 1
        else:
            sorted_array[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        sorted_array[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        sorted_array[k] = right_half[j]
        j += 1
        k += 1

    return sorted_array
