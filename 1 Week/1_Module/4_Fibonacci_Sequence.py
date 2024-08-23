def fibonacchiSequence(n):
    # print(n)
    if n==0:
        return 0;
    elif n==1:
        return 1;
    else:
        return ((fibonacchiSequence(n-1))+(fibonacchiSequence(n-2)));

print(fibonacchiSequence(8)); 