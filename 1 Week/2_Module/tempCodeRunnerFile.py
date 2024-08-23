
number = int(input())
for i in range(1, number + 1):
    # For Spaces
    for s in range(i, number):
        print(" ", end="")
    print(i, end="")

    # For Increasing Number
    k = i + 1
    for n in range(1, i):
        print(k, end="")
        k += 1

    # For Decreasing Number
    x=k-1;
    for m in range(x, i,-1):
        x=x-1;
        print(x, end="")
        
    print()
