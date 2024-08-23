def isSorted(lst,index):
    l=len(lst)
    if index==l-1 or l==index:
        return True;
    elif lst[index]>lst[index+1]:
        return False;
    isSmallerListSorted=isSorted(lst,index+1);
    
    if isSmallerListSorted:
        return True;
    else:
        return False
    
a=[]
print(isSorted(a,0))