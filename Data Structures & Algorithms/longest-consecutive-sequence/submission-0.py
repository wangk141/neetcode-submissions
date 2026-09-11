class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # cannot sort otherwise thats nlogn
        # hashmap?

        dct = {}
        for i in range(len(nums)):
            dct[nums[i]] = i
        retCount = 0
        for i in nums:
            counter = 1
            while i + counter in dct:
                counter += 1
            retCount = max(counter, retCount)
        return retCount