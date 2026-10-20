# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        self.tail = dummy          

        def inorder(node):
            if node is None:
                return
            inorder(node.left)

            node.left = None           
            self.tail.right = node     
            self.tail = node          

            inorder(node.right)

        inorder(root)
        return dummy.right