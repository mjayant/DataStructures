class Tree(object):
    """

    """
    def __int__(self, root):
        """

        :return:
        """
        self.root = root
        self.left = None
        self.right = None

    def insertLeft(self, root):
        """

        :param root:
        :return:
        """
        tree_obj = Tree(root)
        if self.left:
            t = self.left
            self.left = tree_obj
            tree_obj.left = t

        else:
            self.left = tree_obj

    def insertRight(self, root):
        """

        :param root:
        :return:
        """
        tree_obj = Tree(root)
        if self.right:
            t = self.right
            self.left = tree_obj
            tree_obj.left = t
        else:
            self.right = tree_obj

    def getLeft(self):
        """

        :return:
        """
        return self.left

    def getRight(self):
        """

        :return:
        """
        return self.right

    def getRootVal(self):
        """

        :return:
        """
        return self.root

    def setRootVal(self, val):
        """

        :param root:
        :param val:
        :return:
        """
        self.root = val

