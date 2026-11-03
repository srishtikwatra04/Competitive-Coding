class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Example
solution = Solution()

n = 5
print("Number of ways:", solution.climbStairs(n))