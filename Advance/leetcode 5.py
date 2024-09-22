# Define the Solution class
class Solution(object):
    def longestPalindrome(self, s):
        max_length = 0
        max_palindrome = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    if len(substring) > max_length:
                        max_length = len(substring)
                        max_palindrome = substring
        return max_palindrome

# Create an instance of the Solution class
sol = Solution()

# Call the longestPalindrome method with a string argument
input_string = "cbbd" 
result = sol.longestPalindrome(input_string)

# Print the result
print("Longest Palindrome:", result)
