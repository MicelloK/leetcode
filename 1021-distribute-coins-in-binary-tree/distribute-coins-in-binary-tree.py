# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def visit(node: TreeNode) -> Tuple[int, int]:
            num_of_moves = 0
            num_of_nodes = 1
            num_of_coins = node.val
            if node.left:
                left_moves, left_nodes, left_coins = visit(node.left)
                num_of_moves += left_moves
                num_of_nodes += left_nodes
                num_of_coins += left_coins
                if left_nodes > left_coins:
                    num_of_moves += left_nodes - left_coins
            if node.right:
                right_moves, right_nodes, right_coins = visit(node.right)
                num_of_moves += right_moves
                num_of_nodes += right_nodes
                num_of_coins += right_coins
                if right_nodes > right_coins:
                    num_of_moves += right_nodes - right_coins
            if num_of_coins > num_of_nodes:
                num_of_moves += num_of_coins - num_of_nodes

            return num_of_moves, num_of_nodes, num_of_coins

        result, _, _ = visit(root)
        return result