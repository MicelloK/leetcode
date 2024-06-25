# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def rek(node: TreeNode, parent_val: int):
            if node.right:
                node.val += rek(node.right, parent_val)
            else:
                node.val += parent_val
            if node.left:
                left_val = rek(node.left, node.val)
                return left_val
            return node.val

        rek(root, 0)
        return root
            