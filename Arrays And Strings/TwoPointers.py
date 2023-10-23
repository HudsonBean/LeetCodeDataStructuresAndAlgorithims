# The "Two Pointers Method" is a way of linearly searching a list by creating a loop that checks the ends of the list and moves to the middle

# In this program we will create a palindrome checker

def checkIfPalindrome(word: str):
    left = 0
    right = len(word) - 1
    while (left < right):
        if (word[left] != word[right]):
            return False
        else:
            left += 1
            right -= 1
        return True


print(checkIfPalindrome("racecar"))
