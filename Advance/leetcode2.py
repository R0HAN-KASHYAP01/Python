# Define the Solution class
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        answer = []
        for i in range(len(s)):
            result = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j] or j == len(s):
                    answer.append(result)
                    break
                else:
                    result += 1
                    
        if answer:
            return max(answer)
        else:
            return len(s)

# Create an instance of the Solution class
sol = Solution()

# Call the lengthOfLongestSubstring method with a string argument
input_string = "aab"
result = sol.lengthOfLongestSubstring(input_string)

# Print the result
print("Length of the longest substring without repeating characters:", result)
