def towerOfHanoi(n, source, help, destination):
    if n == 1:
        print("Move disk 1 from rod", source, "to destination ", destination)
        return 1
    count = towerOfHanoi(n - 1, source, destination, help)
    print("Move disk", n, "from rod", source, "to destination", destination)
    count += towerOfHanoi(n - 1, help, source, destination)
    return count + 1


n = int(input())
print(towerOfHanoi(n, 1, 2, 3))
