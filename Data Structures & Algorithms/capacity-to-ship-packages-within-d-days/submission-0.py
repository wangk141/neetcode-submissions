class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def count(cap: int) -> int:
            need, tmp = 1, 0
            for w in weights:
                if tmp + w > cap:
                    need += 1
                    tmp = 0
                tmp += w
            return need

        while l < r:
            mid = (l + r) // 2
            if count(mid) <= days:
                r = mid
            else:
                l = mid + 1
        return l