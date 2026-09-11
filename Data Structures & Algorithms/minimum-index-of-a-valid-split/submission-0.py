class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dct = {}
        # find the dominant number
        for num in nums:
            dct[num] = 1 + dct.get(num, 0)
        
        max_val = 0
        ky = -1
        for key in dct:
            if dct[key] > max_val:
                max_val = dct[key]
                ky = key
        counter = 0
        
        for i in range(len(nums) - 1):
            if nums[i] == ky:
                counter += 1
            left = i + 1
            right = len(nums) - i - 1
            right_c = max_val - counter

            if counter * 2 > left and right_c * 2 > right:
                return i
        return -1