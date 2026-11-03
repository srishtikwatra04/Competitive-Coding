
def find_duplicate_brute_force(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return -1


nums = list(map(int, input("Enter the array elements separated by space: ").split()))

duplicate = find_duplicate_brute_force(nums)

print("Duplicate number:", duplicate)