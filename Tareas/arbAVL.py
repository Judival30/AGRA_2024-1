import random
import time
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        balance = self.get_balance(root)
        #print(root.key)
        # Rotaciones para el balanceo
        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        
        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        
        return root
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        
        return x
    
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def delete(self, root, key):
        if not root:
            return root
        
        elif key < root.key:
            root.left = self.delete(root.left, key)
        
        elif key > root.key:
            root.right = self.delete(root.right, key)
        
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            
            elif not root.right:
                temp = root.left
                root = None
                return temp
            
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        
        if not root:
            return root
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        balance = self.get_balance(root)
        
        # Rotaciones para el balanceo después de la eliminación
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        
        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        
        return root
    
    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, root, key):
        if root.key == key:
            return True
        if not root:
            return False
        if root.key < key:
            return self.search(root.right, key)
        
        return self.search(root.left, key)


    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, "balance: ", self.get_balance(root))
            self.inorder_traversal(root.right)

if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None
    
    keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    arb1 = [random.randint(-1000, 1000) for _ in range(10)]
    arb2 = [random.randint(-10000, 10000) for _ in range(100)]
    arb3 = [random.randint(-100000, 100000) for _ in range(1000)]
    avls = [arb1, arb2, arb3]
    cont = 1
    tiempos = []
    for a in avls:
        timeIni = time.perf_counter()
        for key in a:
            root = avl_tree.insert(root, key)

        for key in a:
            avl_tree.search(root, key)

        avl_tree.inorder_traversal(root)
        for key in a:
            root = avl_tree.delete(root, key)
        timefin = time.perf_counter()
        tiempos.append(timefin - timeIni)
       
        root = None
    for t in tiempos:
        print("Tiempo arbol %d: %0.30f" % (cont, t))
        cont+= 1
        
    
    
    
