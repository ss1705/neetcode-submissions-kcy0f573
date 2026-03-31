class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            curr = min(prev1, prev2) + cost[i]
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)