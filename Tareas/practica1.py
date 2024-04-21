from sys import stdin as st
import time

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

def main():
    l = list(map(int, st.readline().split()))
    lb = list(map(int, st.readline().split()))
    l = mergeSort(l)
    #print(l)
    promedio = 0
    tEsta = 0
    promEsta = 0
    tNoEsta = 0
    promNoEsta = 0
    for i in range(len(lb)):
        inicio = time.time()
        t = (binarySearch(l, lb[i]))
        fin = time.time()
        if t == -1:
            tNoEsta += fin - inicio
            promNoEsta += 1
        else:
            tEsta += fin - inicio
            promEsta += 1
        promedio += fin - inicio
        print("buscar", lb[i], "Esta en", t)
    promedio /= 100
    tEsta /= promEsta
    tNoEsta /= promNoEsta
    print("promedio total: %0.30f" % (promedio))
    print("Promedio de datos que no estan %0.30f" % (tNoEsta))
    print("Promedio de datos que estan %0.30f" % (tEsta))
		

main()
