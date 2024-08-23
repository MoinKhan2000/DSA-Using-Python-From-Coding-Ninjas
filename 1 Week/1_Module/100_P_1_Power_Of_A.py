def powerOfNumber(n,p):
    if p==0:
        return 0;
    elif p==1:
        return n;
    else:
        return n*powerOfNumber(n,p-1);

a, b = input().split()
a = int(a)
b = int(b)

print(powerOfNumber(a,b));