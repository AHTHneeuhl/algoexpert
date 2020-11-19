# Time O(N^2) | Space O(N)
def isPalindrome(string):
    reverseString = ""
    for i in reversed(range(len(string))):
        reverseString += string[i]
    return string == reverseString

# Time O(N) | Space O(N)
def isPalindrome(string):
    reverseChars = []
    for i in reversed(range(len(string))):
        reverseChars.append(string(i))
    return string == "".join(reverseChars)

# Time O(N) | Space O(N)
def isPalindrome(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)

# Time O(N) | Space O(1)
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
