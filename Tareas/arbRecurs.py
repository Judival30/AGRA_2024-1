"""
    Implementación de arboles binarios por medio de listas
    Juan Diego Valencia alomia
"""

lst = [2, [3, [1, None, None], [7, None, None]], [5, None, None]]
lst2 = [10, 
        [7, [4, None, None], 
            [9, None, None]], 
        [15,[11, None, None], 
            [20, None, None]]]

def preOrder(lst):
    if lst == None:
        return
    print(lst[0], end=" ")
    preOrder(lst[1])
    preOrder(lst[2])


def postOrder(lst):
    if lst == None:
        return
    postOrder(lst[1])
    postOrder(lst[2])
    print(lst[0], end=" ")


def inOrder(lst):
    if lst == None:
        return
    inOrder(lst[1])
    print(lst[0], end=" ")
    inOrder(lst[2])
    
def binSearch(tree, val):
    if tree is None:
        return False
    elif tree[0] == val:
        return True
    elif tree[0] > val:
        return binSearch(tree[1], val)
    else:
        return binSearch(tree[2], val)

def insertArb(tree, val):
    if tree is None:
        return [val, None, None]
    elif tree[0] > val:
        return [tree[0], insertArb(tree[1], val), tree[2]]
    else:
        return [tree[0], tree[1], insertArb(tree[2], val)]
    
    
preOrder(lst)
print()
inOrder(lst)
print()
postOrder(lst)
print()
print(binSearch(lst2, 20))
print(insertArb(lst2, 12))