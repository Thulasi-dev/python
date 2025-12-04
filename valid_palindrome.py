// Valid Palindrome

// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
// it reads the same forward and backward. Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        # Move left pointer to next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1

        # Move right pointer to previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters in lowercase
        if s[left].lower() != s[right].lower():
            return False

        # Move both pointers
        left += 1
        right -= 1

    return True


// Input: s = "A man, a plan, a canal: Panama"
// Output: true


