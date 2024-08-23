def countNumberOfZerosRecursively(number):
    if number == 0:
        return 0
    elif (number % 10) == 0:
        return 1 + countNumberOfZerosRecursively(number // 10)
    else:
        return countNumberOfZerosRecursively(number // 10)


num = 120001010
print(countNumberOfZerosRecursively(num))
