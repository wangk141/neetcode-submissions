class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # iterate through and store the val no?

        seen = set()

        for i in nums:
            if i in seen:
                return i
            seen.add(i)

        return -1