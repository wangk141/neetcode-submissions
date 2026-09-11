class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        up, down = 1, 1
        maxLen = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up += 1
                down = 1
            elif nums[i] < nums[i - 1]:
                up = 1
                down += 1
            else:
                up, down = 1, 1
            maxLen = max(up, down, maxLen)
        return maxLen

