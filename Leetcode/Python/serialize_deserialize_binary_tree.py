class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "N"
        def pre(root, preaccum):
            if root is None:
                return preaccum

            leftpre = pre(root.left, preaccum)
            rightpre = pre(root.right, preaccum)
            x = [str(root.val)]
            if len(leftpre):
                x.append(leftpre)
            else:
                x.append('N')
            if len(rightpre):
                x.append(rightpre)
            else:
                x.append('N')
            preaccum = ','.join(x)
            return preaccum
        return pre(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = data.split(',')
        def getBT(prel, prer):
            if prer < prel:
                return None
            if prer == prel:
                if preorder[prer] == 'N':
                    return None
                else:
                    return TreeNode(preorder[prer])
            terr, i = 1, 0
            while i < terr:
                if preorder[prel + 1 + i] != 'N':
                    terr += 2
                i += 1

            leftTree = getBT(prel + 1, prel + terr)
            rightTree = getBT(prel + terr + 1, prer)
            root = TreeNode(preorder[prel])
            root.left = leftTree
            root.right = rightTree
            return root
        return getBT(0, len(preorder) - 1)
