class Node(object):
    """

    """
    def __init__(self, data):
        """

        :param prev:
        :param next:
        :param data:
        """
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkedList(object):
    """

    """

    def __init__(self):
        """

        """
        self.head = None

    def append_at_head(self, data):
        """

        :param data:
        :return:
        """
        node = Node(data)
        if not self.head:
             self.head = node
             node.next = None
             node.prev = None

    def append_after(self, prev,  data):
        """

        :param data:
        :return:
        """
        node = Node(data)
        node.prev = prev
        node.next = prev.next
        prev.next = node

    def append_at_end(self, data):
        """

        :param data:
        :return:
        """
        node = Node(data)
        item = self.head
        while (item.next):
            item = item.next

        node.prev = item
        node.next = None
        item.next = node


    def deleteHead(self):
        if  not self.head:
            print ("Linked list is empty")

            return

        if self.head.next == None:
            self.head = None

    def delete(self, data):
        """

        :param data:
        :return:
        """
        if  not self.head:
            print ("Linked list is empty")
            return
        if self.head.next == None:
            self.deleteHead()

        item = self.head
        flag = False
        while(item.next):
            if item.data == data:
                flag = True
                break
            item = item.next
        if not flag:
            print ("Data node is note persent in linked list")
            return
        if flag and item.next==None:
            item.prev.next = None
        elif flag:
            item.prev.next = item.next
            item.next.prev = item.prev


