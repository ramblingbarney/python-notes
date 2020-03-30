def getMaxElementIndexes(a, rotate):
    maxpos = max(range(len(a)), key=a.__getitem__)
    return [(maxpos-r) % len(a) for r in rotate]


x = getMaxElementIndexes([1, 2, 3], [1, 2, 3, 4]) # [1, 0, 2, 1]
# x = getMaxElementIndexes([1, 2, 4, 3], [0, 2]) # [2, 0]
print(x)
