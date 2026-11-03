class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0

            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

           
            current_max = node.val + left_gain + right_gain

            
            maxSum = max(maxSum, current_max)

            
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return maxSum
