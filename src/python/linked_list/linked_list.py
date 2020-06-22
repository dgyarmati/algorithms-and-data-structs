class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.data == other.data
        return False


class LinkedList:
    def __init__(self, items: list = None):
        self.head = None

        if items:
            self.head = Node(items[0])
            node = self.head
            for i in range(len(items)):
                if i > 0:
                    node.next = Node(items[i])
                    node = node.next

    def __repr__(self) -> str:
        nodes = []
        node = self.head

        while node:
            nodes.append(str(node.data))
            node = node.next

        return " -> ".join(nodes)

    def __eq__(self, other):
        if isinstance(other, LinkedList):
            node = self.head
            other_node = other.head
            while node:
                if node.data == other_node.data:
                    return node == other_node
            return True
        else:
            return False

    def __iter__(self) -> Node:
        node = self.head

        while node:
            yield node
            node = node.next

    def find(self, data) -> Node:
        node = self.head

        while node:
            if node.data == data:
                return node
            node = node.next

        return None

    # TODO find other implementation
    # TODO Java, C? JS implementation
    # TODO recursive solution
    def delete_node(self, data):
        if not self.head:
            raise Exception("Linked List is empty!")

        if data == self.head.data:
            node = self.head
            self.head = self.head.next
            return node

        previous_node = self.head
        for node in self:
            if node.data == data:
                if node.data == data:
                    previous_node.next = node.next
                    return node
            previous_node = node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head

            while node.next:
                node = node.next

            node.next = Node(data)

    # naive solution w buffer - O(N)
    def remove_duplicates(self):
        if not self.head:
            raise Exception("Linked List is empty!")

        node = self.head
        duplicates = set()
        previous = None

        while node:
            if node.data in duplicates:
                previous.next = node.next
            else:
                duplicates.add(node.data)
                previous = node
            node = node.next

    # naive solution w runner- O(N^2), space complexity: 1
    def remove_duplicates_with_runner(self):
        if not self.head:
            raise Exception("Linked List is empty!")
        node = second_node = self.head
        while node:
            while second_node.next:
                if node.data == second_node.next.data:
                    second_node.next = second_node.next.next
                else:
                    second_node = second_node.next
            node = second_node = node.next

    # iterative solution, O(n) time and O(1) space
    def get_kth_to_last(self, k):
        if not self.head:
            raise Exception("Linked List is empty!")
        node1 = node2 = self.head

        for i in range(k):
            if node1.next:
                node1 = node1.next
            else:
                return None

        while node1:
            node1 = node1.next
            node2 = node2.next

        return node2


