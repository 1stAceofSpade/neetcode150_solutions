# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        state = []
        def sortbst(root):
            if not root:
                return
            sortbst(root.left)
            state.append(root.val)
            sortbst(root.right)
        sortbst(root)
        return state[k-1]