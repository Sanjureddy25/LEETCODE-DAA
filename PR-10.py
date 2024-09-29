def coin_change(coins, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    for i in range(1, target_sum + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[target_sum] if dp[target_sum] != float('inf') else -1
# Example input:
coins = [1, 2, 5]
target_sum = 11

# Calling the function:
result = coin_change(coins, target_sum)

# Output:
print(result)  # Output: 3 (because 11 = 5 + 5 + 1, minimum 3 coins)
