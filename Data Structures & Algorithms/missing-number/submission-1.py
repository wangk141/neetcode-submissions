class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        for i in range(len(nums)):
            if nums[i] != counter:
                return counter
            counter += 1
        return counter