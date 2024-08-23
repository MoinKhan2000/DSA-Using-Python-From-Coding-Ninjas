def sumOfArrayRecursive(lst):
    if len(lst)==0:
        return 0;
    sum=sumOfArrayRecursive(lst[1:])
    return lst[0]+sum;

lst=[1,2,3,4,5]
print(sumOfArrayRecursive(lst))