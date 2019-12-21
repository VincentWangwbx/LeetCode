# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.
# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s):
        '''def lengthOfLongestSubstring(self, s: str) -> int:'''
        print(s)
        count = 0
        result = 0
        appeared = {}
        mark = 0
        for key, value in enumerate(s):
            if value not in appeared:
                count += 1
                appeared[value] = key
            else:
                if appeared[value] >= mark:
                    count = key - appeared[value]
                    mark = appeared[value]
                else:
                    count += 1
                appeared[value] = key

            result = max(result, count)            
        return result


if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s1))
    print(solution.lengthOfLongestSubstring(s2))
    print(solution.lengthOfLongestSubstring(s3))
    print(solution.lengthOfLongestSubstring("dvdf"))
    print(solution.lengthOfLongestSubstring("tmmzuxt"))
    print(solution.lengthOfLongestSubstring("mmzuxt"))
    print(solution.lengthOfLongestSubstring("mmzuxtz"))
    print(solution.lengthOfLongestSubstring("bbtablud"))
    print(solution.lengthOfLongestSubstring("abba"))
