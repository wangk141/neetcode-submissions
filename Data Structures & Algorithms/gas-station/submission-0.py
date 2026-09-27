class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # idea is we know theres a solution somewhere so just keep incrementing starting point till we hit
        if sum(gas) < sum(cost):
            return -1 
        
        total = 0
        res = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        return res