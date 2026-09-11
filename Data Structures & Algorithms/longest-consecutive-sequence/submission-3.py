class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sliding window
        dct = {}
        for i in range(len(nums)):
            dct.update({nums[i] : 1})
        maxLen = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in dct:
                counter = 1
                while nums[i] + counter in dct:
                    counter += 1
                maxLen = max(maxLen, counter)
        return maxLen