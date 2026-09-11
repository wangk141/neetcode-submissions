class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # idea is to insert in array with values filled maybe
        # eg 2 4 5 8, k = 2, x = 6
        # 0 2 0 4 5 0 x 0 8
        # attempt to code
        # failed too slow

        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x-arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l:r + 1]
        