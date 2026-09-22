def coin_change_min_coins(coins: list[int], amount: int) -> tuple[int, list[int]]:
    """Calculates the minimum number of coins needed to make 'amount'
    and reconstructs the list of coins used.
    
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    # Initialize DP table with infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case

    # Parent table to keep track of the coin used at each step
    parent = [-1] * (amount + 1)

    # Fill the DP array from 1 up to 'amount'
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    # If target amount is unachievable
    if dp[amount] == float('inf'):
        return -1, []

    # Reconstruct the exact coins used
    used_coins = []
    curr = amount
    while curr > 0:
        used_coins.append(parent[curr])
        curr -= parent[curr]

    return int(dp[amount]), used_coins


if __name__ == "__main__":
    available_coins = [1, 2, 5]
    target_amount = 11

    min_coins, coin_combination = coin_change_min_coins(available_coins, target_amount)

    if min_coins != -1:
        print(f"Target Amount:        {target_amount}")
        print(f"Available Denominations: {available_coins}")
        print(f"Minimum Coins Needed: {min_coins}")
        print(f"Coins Used:           {coin_combination}")
    else:
        print(f"Amount {target_amount} cannot be made with coins {available_coins}")
