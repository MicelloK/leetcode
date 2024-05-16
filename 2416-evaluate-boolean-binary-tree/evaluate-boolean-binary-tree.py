# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def eval(node: Optional[TreeNode]) -> bool:
            if node.val < 2:
                return node.val
            if node.val == 2:
                left_eval = eval(node.left)
                if left_eval == 1:
                    return True
                right_eval = eval(node.right)
                return left_eval or right_eval
            if node.val == 3:
                left_eval = eval(node.left)
                if left_eval == 0:
                    return False
                right_eval = eval(node.right)
                return left_eval and right_eval
        return eval(root)
        