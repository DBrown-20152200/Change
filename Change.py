def find_fewest_coins(coins, target):
    if type(target) == list:
        int_target = 0
        for i in range(len(target)):
            int_target += target[i]
        target = int_target
    elif type(target != int):
        ValueError("Target is not a number")
        
    coins.sort(reverse = True)    
    total = []    
    while target != 0:
        for denominations in range(len(coins)):
            if target >= coins[denominations]:
                target -= coins[denominations]
                total.append(coins[denominations])
            else:
                denominations += 1
    total.sort()
    return total