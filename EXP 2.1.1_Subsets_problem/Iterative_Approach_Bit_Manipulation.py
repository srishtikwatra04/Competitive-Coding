from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        n = len(nums)
        for mask in range(1 << n):
            subset = []

            for i in range(n):

                if mask & (1 << i):
                    subset.append(nums[i])

            result.append(subset)

        return result


nums = list(map(int, input("Enter elements separated by space: ").split()))

solution = Solution()

answer = solution.subsets(nums)

print("All subsets:")
print(answer)

print("Total subsets:", len(answer))