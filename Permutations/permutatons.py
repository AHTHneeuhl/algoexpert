# Time O(N^2 * N!) | Space O(N * N!)
def get_permutations(array):
    permutations = []
    permutations_helper(array, [], permutations)
    return permutations

def permutations_helper(array, current_permutations, permutations):
    if not len(array) and len(current_permutations):
        permutations.append(current_permutations)
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i + 1:]
            new_permutations = current_permutations + [array[i]]
            permutations_helper(new_array, new_permutations, permutations)