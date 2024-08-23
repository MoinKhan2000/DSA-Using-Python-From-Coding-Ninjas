# if n is even : x^n= x^(n/2)* x^(n/2)
# if n is odd : x^n= x^(n/2)* x^(n/2)*n
def power(n, x):
    if x == 0:
        return 1
    elif x == 1:
        return n
    if x % 2 == 0:
        # return power(n, x / 2) * power(n, x / 2)
        # Recurrence relation if we use this approach T(n)=k+2T(n/2)===O(n)
        # Using this approach time complexity will not be changesd.Instead of calling the same function twise we should store it's output and use it.

        # Recurrence Relation For this T(n)=k+T(n/2)===O(log n)
        halfRes = power(n, x / 2)
        return halfRes * halfRes
    else:
        # return power(n, x // 2) * power(n, x // 2) * n
        # Recurrence relation if we use this approach T(n)=k+2T(n/2)===O(n)
        # Using this approach time complexity will not be changesd.Instead of calling the same function twise we should store it's output and use it.

        # Recurrence Relation For this T(n)=k+T(n/2)=== Time Complexity - O(log n) Space Complexity - O(log n)

        halfRes = power(n, x // 2)
        return halfRes * halfRes * n


print(power(2, 4))
print(power(2, 13))
