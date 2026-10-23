# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def checkGood(root , maxPrev):
            if root is None:
                return 0
            good = 0
            if root.val >= maxPrev:
                good = 1
            
            newMax = max(maxPrev,root.val)
            good += checkGood(root.left,newMax)
            good += checkGood(root.right,newMax)

            return good
        return  checkGood(root, float('-inf'))   
        