#3. Binary Search Tree

import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    
    if value == root.value:
        return True
    if value < root.value and root.left == None:
        return False
    if value >= root.value and root.right == None:
        return False
    if value != root.value and root.left == None and root.right == None:
        return
    else:
        if value < root.value:
            return contains(root.left, value)
        elif value >= root.value:
            return contains(root.right, value)
   
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))
