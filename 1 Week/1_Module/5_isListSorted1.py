def isSorted(lst):
    l=len(lst)
    if l==0 or l==1:
        return True;
    elif lst[0]>lst[1]:
        return False
    smallerList=lst[1:];
    isSmallerListSorted=isSorted(smallerList);
    
    if isSmallerListSorted:
        return True;    
    else:
        return False
    
a=[1,2,3,4,8,12,142] 
print(isSorted(a))
    
# 
"""def isSortedFor(lst):
    for i in range(0, len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    return True
            
    
a=[1,2,3,3,4,8,12,142]
print(isSortedFor(a))"""