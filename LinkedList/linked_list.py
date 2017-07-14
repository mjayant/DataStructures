class Node(object):
    """
    This class for linked list node each object of this class
    is item of linked list
    """

    def __init__(self, data):
        """

        :param data:
        """
        self.data = data
        self.next = None

    def __str__(self):
        """

        :return:
        """
        return "Node[Data=" + str(self.data) + "]"

class LinkedList(object):
    """
    This class for linked list , it has all functions and variable related to
    linked list.
    """

    def __init__(self, data):
        """

        :param data:
        """
        self.data = data
        self.head = None

    def append_at_head(self, data):
        """
        This funtion will append node at head
        :param data:
        :return:
        """

        node_obj = Node(data)

        if not self.head:
            self.head = node_obj
        else:
            node_obj.next = self.head
            self.head = node_obj

    def append_after(self, prev_node, data):
        """

        :param data:
        :return:
        """
        if not prev_node:
            print ("Please give previsous node")
            return

        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node

    def append_at_end(self, data):
        """

        :param data:
        :return:
        """
        node = Node(data)
        item = self.head

        while (item.next):

            item = item.next

        item.next = node
        node.next = None

    def show_node(self):
        """

        :return:
        """
        item = self.head
        while (item.next):
            print(item)
            item = item.next

    def delete(self, data):
        """

        :param data:
        :return:
        """
        item = self.head
        prev = ''
        while(item.next):
            if item.data ==  data:
                break
            prev = item
            item = item.next

        prev.next = item.next



# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.append_at_end(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.append_at_head(7);

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.append_at_head(1);

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append_at_end(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.append_after(llist.head.next, 8)

    print
    'Created linked list is:',
    llist.show_node()
