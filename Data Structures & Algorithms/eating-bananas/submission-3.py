import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        minEaten = max(piles)
        while left <= right:
            midpoint = left + (right - left) // 2
            if midpoint == 0:
                break
            finishSpeed = sum(math.ceil(i / midpoint) for i in piles)
            if finishSpeed <= h and midpoint < minEaten:
                minEaten = midpoint
                right = midpoint - 1
            else:
                left = midpoint + 1
        return minEaten