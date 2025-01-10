# How many ways can you make change with coins and a total amount
# Given coin denominations [1,2,5] and the total amount is 5
# Basically we have coins 1,2 and 5 how many combination is the sum of 5
# Create a solution list of size amount+1
# set solution[0] = 1 because there is one way to make amount 0: with no coins
# outer loop: iterate each coin in the denomination list, calculate number of way to make amount up to the target
# inner loop: update the solution list: loop from value of current coin to amount+1
    # for each value i: add number of ways to make the denom 
    # update solution to reflect additional way to make amount 
# repeat for all denominations

def solve_coin_change(denominations, amount):
    solution = [0] * (amount + 1)
    solution[0] = 1 #init
    for den in denominations:
        for i in range(den, amount + 1):
            solution[i] += solution[i - den]

    return solution[len(solution) - 1]

denominations = [1,2,5]
amount = 5

print(solve_coin_change(denominations,amount))
# 4

denominations = [1,2,3,4]
amount = 20
print(solve_coin_change(denominations,amount))
#108

denominations = [1,2]
amount = 3
print(solve_coin_change(denominations,amount))
#2

# Time complexity
# Outer loop iterates over all denominations: O(d), where d is the number of denominations
# Inner loop iterates up to amount+1: O(amount)
# Total complexity: O(d×amount)

# Space complexity
# O(amount)
