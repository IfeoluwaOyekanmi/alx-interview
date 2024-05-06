#!/usr/bin/python3
"""
Main file for testing
"""
def makeChange(coins, total):
    if total <= 0:
        return 0
   
    # Initialize an array to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
   
    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each total from the value of the current coin
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
   
    # If the total can't be met by any combination of coins, return -1
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total] 