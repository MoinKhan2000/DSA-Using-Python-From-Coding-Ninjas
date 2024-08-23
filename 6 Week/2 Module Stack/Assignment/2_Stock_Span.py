from sys import stdin


def stockSpan(price, n):
    stack = []
    output = []
    for i in range(len(price)):
        if len(stack) == 0:
            stack.append([price[i], i])
            output.append(-1)
        elif len(stack) > 0 and stack[-1][0] > price[i]:
            output.append(stack[-1][1])
            stack.append([price[i], i])
        elif len(stack) > 0 and stack[-1][0] <= price[i]:
            while len(stack) > 0 and price[i] > stack[-1][0]:
                stack.pop(len(stack) - 1)
            if len(stack) == 0:
                output.append(-1)
            else:
                output.append(stack[-1][1])
            stack.append([price[i], i])
    for i in range(len(price)):
        output[i] = i - output[i]

    return output


"""-------------- Utility Functions --------------"""


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

    print()


def takeInput():
    size = int(stdin.readline().strip())

    if size == 0:
        return list(), 0

    price = list(map(int, stdin.readline().strip().split(" ")))

    return price, size


# main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
