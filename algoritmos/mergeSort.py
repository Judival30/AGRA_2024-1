def merge(l : list, r : list):
    ans = []
    lid = 0
    rid = 0
    while lid < len(l) and rid < len(r):
        if l[lid] < r[rid]:
            ans.append(l[lid])
            lid += 1
        else:
            ans.append(r[rid])
            rid += 1

    while lid < len(l):
        ans.append(l[lid])
        lid += 1
    while rid < len(r):
        ans.append(r[rid])
        rid += 1
    return ans


def mergeSort(l):
    if len(l) == 1:
        return l
    m = len(l) // 2
    left = l[:m]
    rigth = l[m:]
    left = mergeSort(left)
    rigth = mergeSort(rigth)
    
        
    return merge(left, rigth) 
