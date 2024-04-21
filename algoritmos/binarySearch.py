def binarySearch(lst, d):
    l = 0
    r = len(lst) - 1
    ans = -1
    flag = True
    while l < r and flag:
        m = (l + r) // 2
        if lst[m] == d:
            ans = m
            flag = False
        elif lst[m] < d:
            l = m + 1
        else:
            r = m -1
    return ans 
