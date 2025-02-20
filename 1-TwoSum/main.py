nums = [2, 7, 11, 15]
target = 9
# O(n)
"""
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[num] = i

solution = Solution()

print(f"A megoldas: {solution.twoSum(nums, target)}")
"""

#O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
                
solution = Solution()

print(f"A megoldas: {solution.twoSum(nums, target)}")