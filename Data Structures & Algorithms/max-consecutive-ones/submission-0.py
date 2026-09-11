class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            if nums[i] == 0:
                max_num = max(counter, max_num)
                counter = 0
        return max(max_num, counter)