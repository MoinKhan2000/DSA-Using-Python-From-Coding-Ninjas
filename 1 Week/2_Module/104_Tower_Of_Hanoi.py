def towerofhanoi(n, source, help, destination):
    if n <= 0 :
        return
    if n == 1:
        # print(source, destination)
        return 1
    count = towerofhanoi(n - 1, source, destination, help)
    # print(source, destination)
    count += towerofhanoi(n - 1, help, source, destination)
    return count + 1


n = int(input())
print(towerofhanoi(n, "a", "b", "c"))
