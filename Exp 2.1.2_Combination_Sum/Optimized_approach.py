def combination_sum(candidates, target):

    candidates.sort()
    result = []

    def backtrack(start, remaining, current):

        if remaining == 0:
            result.append(current.copy())
            return

        for i in range(start, len(candidates)):

            # Pruning
            if candidates[i] > remaining:
                break

            # Choose
            current.append(candidates[i])

            # Explore
            backtrack(i, remaining - candidates[i], current)

            # Unchoose
            current.pop()

    backtrack(0, target, [])

    return result


# -------- INPUT --------

n = int(input("Enter number of candidates: "))

candidates = list(map(int, input("Enter candidates: ").split()))

target = int(input("Enter target: "))


# -------- OUTPUT --------

answer = combination_sum(candidates, target)

print("Combinations:", answer)