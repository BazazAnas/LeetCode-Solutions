# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def lvs(root):
            if root is None:
                return []
            if(not root.left and not root.right):
                return [root.val]
            return lvs(root.left) + lvs(root.right)

        l1 = lvs(root1)
        l2 = lvs(root2)

        return l1 == l2    