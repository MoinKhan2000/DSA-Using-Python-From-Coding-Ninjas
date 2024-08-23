"""n = 10
while n > 0:
    print("hii")
    n = n // 4
"""


def sumOfDigits(n):
    if n < 10:
        return n
    sum = (n % 10) + sumOfDigits(n//10)
    return sum
n=350;
print('sum of digits is',sumOfDigits(n))