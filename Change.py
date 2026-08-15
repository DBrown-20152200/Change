def find_fewest_coins(coins, target):
    # checks if target is negative
    if target < 0:
        raise ValueError("target can't be negative")

    # sets up an array with [coins_limit] instances of (target + 1)
    coins_limit = target + 1
    change_array = [coins_limit] * (target + 1)
    change_array[0] = 0

    # loops through array for no. of coins, 
    # adds iterable and coin value to running total,
    # exits loop when coin_limit is reached
    for amount, number_of_coins in enumerate(change_array):
        if number_of_coins == coins_limit:
            continue
        for coin in coins:
            total = amount + coin
            if total <= target:
                change_array[total] = min(change_array[total], number_of_coins + 1)

    # If the array can't reach target value, raise error
    if change_array[target] > target:
        raise ValueError("can't make target with given coins")

    # creates list of coins to reach target
    change = []
    for coin in coins:
        while coin <= target and change_array[target] == change_array[target - coin] + 1:
            change.append(coin)
            target -= coin

    return change