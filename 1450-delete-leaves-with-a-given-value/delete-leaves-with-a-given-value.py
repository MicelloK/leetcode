# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def visit(node: TreeNode) -> bool:
            if not node:
                return True
            if visit(node.left):
                node.left = None
            if visit(node.right):
                node.right = None
            if node.left == None and node.right == None and node.val == target:
                return True
            return False
        
        visit(root)
        if root.val == target and root.left == None and root.right == None:
            return None
        return root
            

            
        