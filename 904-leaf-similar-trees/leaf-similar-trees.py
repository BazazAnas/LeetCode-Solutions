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
        def lvs(root , leaves):
            if root is None:
                return
            if(not root.left and not root.right):
                return leaves.append(root.val)
            lvs(root.left,leaves)
            lvs(root.right,leaves)

        l1 = [] 
        lvs(root1, l1)
        l2 =[]
        lvs(root2, l2)

        return l1 == l2    