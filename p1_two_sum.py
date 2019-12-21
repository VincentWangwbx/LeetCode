# https://leetcode.com/problems/two-sum/
# 1. Two Sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from timer import func_timer

class Solution:
    @func_timer
    def twoSum(self, nums, target):
        '''def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash map, O(n)'''
        dic = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in dic:
                return [dic[other], i]
            else:
                dic[nums[i]] = i    # store (value,index) into hmap, value becomes the key
        return []


if __name__ == '__main__':
    solution = Solution()   
    print(solution.twoSum(nums = [2, 7, 11, 15], target = 9))
