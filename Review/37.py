def maxDiff(a):
    vmin = a[0]
    dmax = 0
    for i in range(len(a)):
        if a[i] < vmin:
            vmin = a[i]
        elif a[i] - vmin > dmax:
            dmax = a[i] - vmin
    return dmax
print (maxDiff(a = [77, -10, 177, 83, 68]))

