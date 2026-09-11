class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the arr and use two pointer
        people.sort()
        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            rem = limit - people[r]
            r -= 1
            res += 1
            if l <= r and rem >= people[l]:
                l += 1
        return res
        # FAILED ATTEMPT TO RECREATE TWO SUM
        # dict = {}
        # for p in people:
        #     if p not in dict:
        #         dict.update({p : 1})
        #     else:
        #         dict[p] += 1
        # counter = 0
        # for p in people:
        #     if dict[p] == 0:
        #         continue

        #     if p == limit:
        #         dict[p] -= 1
        #         counter += 1
        #         continue
        #     elif limit - p in dict:
        #         dict[p] -= 1
        #         dict[limit - p] -= 1
        #         counter += 1
        #     else:
        #         a = closest(dict, limit - p)
        #         if a > 0:
                    
            
        #     # check the remainder
            
        #     def closest(dict, num):
        #         min_n = float("inf")
        #         for value in dict.values:
        #             if min_n > num - value:
        #                 min_n = num - value
        #                 dict[value] -= 1
        #         return min_n

        # return counter