from .. nodes_and_ref_rep.nodes_and_ref_rep import Tree

import re

class ParseTree(object):
    """

    """

    def parsetree(self, exp):
        """

        :param exp:
        :return:
        """
        parse_exp_lst = exp.split(" ")
        parent_node_lst = []

        # Creating first node of tree with empty value
        t_obj = Tree('')

        current_node = t_obj

        for exp_item in parse_exp_lst:
            if '(' in exp_item:
                parent_node_lst.append(t_obj)
                t_obj.insertLeft('')
                current_node = t_obj.getLeft()

            elif re.match('\d+$', exp_item):
                current_node.setRootVal(exp_item)
                current_node = parent_node_lst.pop()

            elif exp_item in ['+', '-', '*', '/']:
                current_node.setRootVal(exp_item)
                parent_node_lst.append(current_node)
                current_node.insertRight('')
                current_node = current_node.getRight()

            elif ')' in exp_item:
                current_node = parent_node_lst.pop()
            else:
                raise ValueError

        return t_obj

    def preorder(self, tree):
        if tree:
            print(tree.getRootVal())
            self.preorder(tree.getLeft())
            self.preorder(tree.getRight())



pt_obj = ParseTree()
t_obj = pt_obj.parsetree("( ( 10 + 5 ) * 3 )")

#t_obj.postorder()
