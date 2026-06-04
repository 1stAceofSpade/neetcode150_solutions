# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def compare(node , subRoot):
            if not node and not subRoot:
                return True
            if not node or not subRoot:
                return False

            return (node.val == subRoot.val and compare(node.left , subRoot.left) and compare(node.right , subRoot.right))


        def dfs(root , val):
            if not root: return False

            return (compare(root , subRoot) or dfs(root.left , subRoot) or dfs(root.right , subRoot))
        

        

        
        return dfs(root , subRoot)


