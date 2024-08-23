# In an online competition the main constraint is time
""" 
A = [1,2,3,4,5] n len
B = [2,4,6,2,3] n len
Now we have to find the Intersection Of A and B 
    First Approach : 
            for i in A:
                for j in B:
                    if i==j:
                        print(j)
                    This is too much time consuming. O(n^2);

"""


# Normally Our Computer Is Able to perform 10^8 Operations in 1 Second
# Suppose if the constaint is given n < (10^6) and our algorithm is taking O(n^2) so this means 10^12 operation per second is not able for the computer to do in 1 second means we have to look for the better solution
