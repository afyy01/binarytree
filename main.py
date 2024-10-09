class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    #if tree is empty (the key itself is a root
    if root is None:
            return Node(key)
        
        #otherwise recur down the tree

    if key < root.val:
            root.left = insert(root.left,key)

    else:
            root.right = insert(root.right , key)

            "return the root pointer"
    return root
        
#example

root = Node(8)
insert(root,3)
insert(root,10)
insert(root,1)
insert(root,6)
insert(root,4)
insert(root,7)
insert(root,5)

def inorder_transversal(root):
    if root:
        inorder_transversal(root.left)
        print(root.val, end = " - ")
        inorder_transversal(root.right)
inorder_transversal(root)

def search(root,key):
        #base case: if the item that u are searching for is the root of the root - reutrn root itself
        if root is None or root.val == key:
              return root
        #if key is greater than root 
        if key > root.val:
              return search(root.right, key)

        #key is smaller than the root 
        return search (root.left, key)

search_node = search(root, 12)
print()
if search_node:
      print(f"{search_node.val} is in the tree")
else:
      print("element not in the tree")


