def knapsack(weights, values, capacity):
    n = len(values)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            current_weight = weights[i - 1]
            current_value = values[i - 1]

            if current_weight <= w:
                dp[i][w] = max(dp[i - 1][w], current_value + dp[i - 1][w - current_weight])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


item_values = [60, 100, 120]
item_weights = [10, 20, 30]
knapsack_capacity = 50

max_value = knapsack(item_weights, item_values, knapsack_capacity)
print(f"Maximum value in Knapsack = {max_value}")  # Output: 220
