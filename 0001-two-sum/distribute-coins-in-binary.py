# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            
            
            left = dfs(root.left)
            right = dfs(root.right)

            root.val += left + right
            ans += abs(root.val - 1)
            return root.val - 1

        dfs(root)
        return ans

            
            

        
