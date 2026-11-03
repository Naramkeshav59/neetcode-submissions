class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n, memo):
            if memo[n] != -1:
                return memo[n]
            memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
            return memo[n]
        
        memo = [-1]*(n+1)  
        memo[0] = 1
        memo[1] = 1
        return helper(n, memo)