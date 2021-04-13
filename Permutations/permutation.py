# Time O(N * N!) | Space O(N * N!)
def get_permutations(array):
    permutations = []
    permutations_helper(0, array, permutations)
    return permutations

def permutations_helper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutations_helper(i + 1, array, permutations)
            swap(array, i, j)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]