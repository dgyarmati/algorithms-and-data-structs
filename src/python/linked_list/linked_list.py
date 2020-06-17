class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


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

    def append(self, data):
        node = self.head

        while node.next:
            node = node.next

        node.next = Node(data)


linked_list = LinkedList([1, 2, 3, 4])
print(linked_list) # 1 -> 2 -> 3 -> 4
linked_list.append(5) # 1 -> 2 -> 3 -> 4 -> 5
print(linked_list.find(6)) # None
