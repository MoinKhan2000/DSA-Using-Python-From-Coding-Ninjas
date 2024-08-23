def sumOfNaturalNumber(n):
    if n==0:
        return 0; 
    else:
        return n+sumOfNaturalNumber(n-1);
    
print(sumOfNaturalNumber(100))
    
    