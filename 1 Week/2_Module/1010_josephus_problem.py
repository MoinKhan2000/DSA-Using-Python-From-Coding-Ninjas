def JosephusProblem(arr, index):
    if len(arr) == 1:
        return arr
    else:
        diePersonIndex = (index - 1) % len(arr)
        arr.pop(diePersonIndex)
        return JosephusProblem(arr, index + 1)


arr = list(range(1, 8))
print(arr)
step = 3
winner = JosephusProblem(arr, step)
print(f"The person who survives in the {len(arr)} person Josephus problem is: {winner}")
