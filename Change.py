def find_fewest_coins(coins, target):
    initial_target = target
    coins.sort(reverse = True)    
    change = [] 
    total = 0   
    while target > 0:
        for denominations in range(len(coins)):
            if target >= coins[denominations]:
                target -= coins[denominations]
                total += coins[denominations]
                change.append(coins[denominations])
            else:
                denominations += 1
        if target != 0:
            raise ValueError("can't make target with given coins")
    
    change.sort()
    return change