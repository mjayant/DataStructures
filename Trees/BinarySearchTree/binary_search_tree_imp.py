class TreeNode(object):
    """

    """

    def __init__(self, key, val):
        """

        :param key:
        :param val:
        """
        self.key = key
        self.val = val
        self.right = None
        self.left = None
        self.parent = None

    def hasRightChild(self):
        """

        :return:
        """
        if self.right:
            return True

    def hasLeftChild(self):
        """

        :return:
        """
        if self.left:
            return True

    def isLeftChild(self):
        """

        :return:
        """
        return self.parent.left == self

    def isRightChild(self):
        """

        :return:
        """
        return self.parent.right == self

    def isRoot(self):
        """

        :return:
        """
        return not self.parent

    def isLeaf(self):
        """

        :return:
        """
        return not (self.left or self.right)

    def hasBothChildren(self):
        """

        :return:
        """
        return self.rightChild and self.leftChild


    def replaceNodeData(self, key, value, lc, rc):
        """

        :param key:
        :param value:
        :param lc:
        :param rc:
        :return:
        """
        self.key = key
        self.val = value
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

