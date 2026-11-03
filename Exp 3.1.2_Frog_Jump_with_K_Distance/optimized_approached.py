def frog_jump(height, k):
    n = len(height)

    #
    dp = [0] * n

    
    for i in range(1, n):
        best = float('inf')

        for j in range(max(0, i - k), i):
            cost = dp[j] + abs(height[i] - height[j])
            best = min(best, cost)

        dp[i] = best

    return dp[n - 1]


height = list(map(int, input("Enter heights: ").split()))
k = int(input("Enter maximum jump distance k: "))

answer = frog_jump(height, k)

print("Minimum cost:", answer)