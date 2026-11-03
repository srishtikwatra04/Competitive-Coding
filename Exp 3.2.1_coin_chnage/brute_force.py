
def coin_change_brute(coins, amount):
    if amount == 0:
        return 0

    min_coins = float('inf')

    for coin in coins:
        if coin <= amount:
            result = coin_change_brute(coins, amount - coin)

            if result != float('inf'):
                min_coins = min(min_coins, result + 1)

    return min_coins


# User input
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))

answer = coin_change_brute(coins, amount)

if answer == float('inf'):
    print("Minimum coins required: -1")
else:
    print("Minimum coins required:", answer)
