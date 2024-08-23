# def update(ans, newAmount, target):
#     if abs(target - ans) > abs(target - newAmount):
#         return newAmount
#     elif abs(target - ans) == abs(target - newAmount):
#         return min(ans, newAmount)
#     else:
#         return ans


# def f(ind, toppings, amount, target, ans):
#     if ind == len(toppings):
#         return update(ans, amount, target)
#     else:
#         forZero = f(ind + 1, toppings, amount, target, ans)
#         forFirst = f(ind + 1, toppings, amount + toppings[ind], target, ans)
#         forSecond = f(ind + 1, toppings, amount + 2 * toppings[ind], target, ans)
#         return min(forZero, forFirst, forSecond)


# def closestCost(n, m, baseCosts, toppingsCost, target):
#     ans = float("inf")
#     for i in range(n):
#         ans = min(ans, f(0, toppingsCost, baseCosts[i], target, float("inf")))
#         print(ans)
#     return ans


# Custom Test Case


def close(a, b, target):
    if a == 0:
        return b
    if b == 0:
        return a

    if abs(target - a) == abs(target - b):
        return a if a < b else b

    return a if abs(target - a) < abs(target - b) else b


def dfs(toppings, i, total, target):
    if i >= len(toppings):
        return total

    a = dfs(toppings, i + 1, total + toppings[i], target)
    b = dfs(toppings, i + 1, total + toppings[i] * 2, target)
    c = dfs(toppings, i + 1, total, target)

    return close(a, close(b, c, target), target)


def closestCost(n, m, base_costs, topping_costs, target):
    ans = 0

    for i in range(n):
        ans = close(dfs(topping_costs, 0, base_costs[i], target), ans, target)

    return ans


baseCostLen = 2
baseCost = [1, 7]
toppingCostsLen = 3
toppingCosts = [1, 2, 3]
target = 10

result = closestCost(baseCostLen, toppingCostsLen, baseCost, toppingCosts, target)
print(result)
