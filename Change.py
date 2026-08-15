def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
         
    coins_limit = target + 1
    dp = [coins_limit] * (target + 1)
    dp[0] = 0

    for amount, number_of_coins in enumerate(dp):
        if number_of_coins == coins_limit:
            continue
        for coin in coins:
            total = amount + coin
            if total <= target:
                dp[total] = min(dp[total], number_of_coins + 1)

    if dp[target] > target:
        raise ValueError("can't make target with given coins")
    
    change = []
    for coin in coins:
        while coin <= target and dp[target] == dp[target - coin] + 1:
            change.append(coin)
            target -= coin

    return change