# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preOrder(root, res)
        return res

    def preOrder(self, root, arr):
        if root:
            arr.append(root.val)
            self.preOrder(root.left, arr)          
            self.preOrder(root.right, arr)