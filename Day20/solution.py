class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bstFromPreorder(preorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    i = 1
    while i < len(preorder) and preorder[i] < root.val:
        i += 1
    root.left = bstFromPreorder(preorder[1:i])
    root.right = bstFromPreorder(preorder[i:])
    return root
    
def InorderTraversal(root):
    if root == None:
        return
    InorderTraversal(root.left)
    print(root.val)
    InorderTraversal(root.right)
    
preorder = [8,5,1,7,10,12]
root = bstFromPreorder(preorder)
InorderTraversal(root)
