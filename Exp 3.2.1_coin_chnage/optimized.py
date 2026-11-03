
def coin_change_optimized(coins, amount):
    # Initialize DP table
    dp = [amount + 1] * (amount + 1)

    # Base case: zero coins needed for amount zero
    dp[0] = 0

    # Calculate minimum coins for each amount
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    # Return -1 if the amount cannot be formed
    return dp[amount] if dp[amount] <= amount else -1


# User input
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))

answer = coin_change_optimized(coins, amount)

print("Minimum coins required:", answer)
