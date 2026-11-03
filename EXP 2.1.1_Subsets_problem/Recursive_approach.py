from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack(start):
        
            result.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])

                backtrack(i + 1)

                current.pop()
        backtrack(0)

        return result

nums = list(map(int, input("Enter elements separated by space: ").split()))

solution = Solution()

answer = solution.subsets(nums)

print("All subsets:")
print(answer)

print("Total subsets:", len(answer))