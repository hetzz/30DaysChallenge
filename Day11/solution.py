# Definition for a binary tree Treenode.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def heightofTree(self,root):
        if root == None:
            return 0
        else:
            return (1 + max(self.heightofTree(root.left), self.heightofTree(root.right)))
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        lheight = self.heightofTree(root.left) 
        rheight = self.heightofTree(root.right) 
        ldiameter = self.diameterOfBinaryTree(root.left) 
        rdiameter = self.diameterOfBinaryTree(root.right) 
        return max(lheight + rheight + 1 , max(ldiameter, rdiameter)) -1

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5)

temp = Solution()
print(temp.diameterOfBinaryTree(root))