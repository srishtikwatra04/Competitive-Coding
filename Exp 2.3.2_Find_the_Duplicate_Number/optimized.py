
def find_duplicate_optimized(nums):

    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow



nums = list(map(int, input("Enter the array elements separated by space: ").split()))

duplicate = find_duplicate_optimized(nums)

print("Duplicate number:", duplicate)