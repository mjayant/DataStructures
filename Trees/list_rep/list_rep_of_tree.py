class ListReprestationTree(object):
    """

    """

    def getTree(self, root):
        """

        :param root: root of tree
        :return: list represtation of tree where 0th element will be root

        """

        return  [root, [], []]

    def insertleft(self, root, element):
        """

        :param root:
        :param element: Which has to be added in tree
        :return: it add to element at left branch of root and return tree
        """

        elem = root[1]
        if len(elem) > 1:
            root.insert(1, [element, elem,  []])
        else:
            root.insert(1, [element, [], []])

    def insertRight(self, root, element):
        """

        :param root:
        :param element: Which has to be added in tree
        :return: it add to element at left branch of root and return tree
        """
        right_node = root[2]
        if len(right_node) > 1:
            root.insert(2, [element, [], right_node ])
        else:
            root.insert(2, [element, [], []])

    def getRootVal(self, root):
        """

        :param root: List represention of tree
        :return: root value for that tree
        """
        return root[0]

    def getLeftNode(self, root):
        """

        :param root:
        :return:
        """
        return root[1]

    def getRightNode(self, root):
        """

        :param root:
        :return:
        """

        return root[2]

