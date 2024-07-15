# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NodeInfo:
    def __init__(self, parent=None, left_child=None, right_child=None):
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {} # {node: {childs: [], parent: x}}
        def build_tree(node_val):
            if not node_val:
                return None
            node = TreeNode(node_val)
            node.left = build_tree(nodes[node_val].left_child)
            node.right = build_tree(nodes[node_val].right_child)
            return node

        for parent, child, is_left in descriptions:
            if parent in nodes:
                if is_left:
                    nodes[parent].left_child = child
                else:
                    nodes[parent].right_child = child
            else:
                if is_left:
                    nodes[parent] = NodeInfo(left_child=child)
                else:
                    nodes[parent] = NodeInfo(right_child=child)
            if child in nodes:
                nodes[child].parent = parent
            else:
                nodes[child] = NodeInfo(parent=parent)

        root = descriptions[0][0]
        while nodes[root].parent:
            root = nodes[root].parent
        
        return build_tree(root)