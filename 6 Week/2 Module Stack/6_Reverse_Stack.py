def reverseStack(inputStack, extraStack):
    while not isEmpty(inputStack):
        # Pop an element from the inputStack
        top = inputStack.pop()

        # Push it onto the extraStack
        extraStack.append(top)

    while not isEmpty(extraStack):
        # Pop an element from the extraStack
        top = extraStack.pop()

        # Push it back onto the inputStack, effectively reversing the order
        inputStack.append(top)


def isEmpty(stack):
    return len(stack) == 0


# Taking input using fast I/o method
def takeInput():
    inputStack = list()
    values = list(map(chr, input().split()))
    inputStack.extend(values)

    return inputStack


# Main
inputStack = takeInput()
emptyStack = list()
reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack):
    print(inputStack.pop(), end=" ")
