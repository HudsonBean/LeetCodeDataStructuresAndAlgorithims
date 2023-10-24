# The "Two Pointers Method" is a way of linearly searching a list by creating a loop that checks the ends of the list and moves to the middle

# In this program we will create a palindrome checker

# This function takes a string and checks if it's a palindrome
def checkIfPalindrome(word: str) -> bool:
    left = 0  # First index of the list
    right = len(word) - 1  # Last index of the list
    while (left < right):  # Check if they aren't at the middle of the string yet
        if (word[left] != word[right]):  # If one of the letters don't match then return false
            return False
        else:
            left += 1  # Increment left and right
            right -= 1
        return True  # Is palindrome


print(checkIfPalindrome("racecar"))
