def combination_sum(candidates, target):

    result = set()

    def solve(remaining, current):

        # Target reached
        if remaining == 0:
            result.add(tuple(sorted(current)))
            return

        # Target exceeded
        if remaining < 0:
            return

        # Try every candidate
        for c in candidates:
            current.append(c)

            solve(remaining - c, current)

            current.pop()

    solve(target, [])

    return [list(combination) for combination in result]


# -------- INPUT --------

n = int(input("Enter number of candidates: "))

candidates = list(map(int, input("Enter candidates: ").split()))

target = int(input("Enter target: "))


# -------- OUTPUT --------

answer = combination_sum(candidates, target)

print("Combinations:", answer)