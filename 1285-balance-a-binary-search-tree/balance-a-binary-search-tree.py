# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def get_nodes(node: TreeNode) -> TreeNode:
            if node.left:
                get_nodes(node.left)
                node.left = None
            nodes.append(node.val)
            if node.right:
                get_nodes(node.right)
                node.right = None
        get_nodes(root)

        def build_bbst(l: int, r: int):
            mid = (l+r) // 2
            new_root = TreeNode(nodes[mid])
            if l < mid:
                new_root.left = build_bbst(l, mid-1)
            if mid < r:
                new_root.right = build_bbst(mid+1, r)
            return new_root
        return build_bbst(0, len(nodes)-1)

        


        