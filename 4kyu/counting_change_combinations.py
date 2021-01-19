#PROBLEM: https://www.codewars.com/kata/541af676b589989aed0009e7

#SOLUTION:
def count_change(money, coins):
    if money == 0:
        return 1
    if money < 0:
        return 0
    count = 0
    for i in range(len(coins)):
        coin = coins[i]
        count += count_change(money - coin, coins[i:])
    return count
