import math
from collections import deque


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

    # recursive solution, O(n) time
    def print_kth_to_last(self, node, k):
        if not node:
            return 0
        idx = self.print_kth_to_last(node.next, k) + 1
        if idx == k:
            print(k, "th last node is", node.data)
        return idx

    def delete_middle_node(self, node):
        if not node or not node.next:
            return None
        node.data = node.next.data
        node.next = node.next.next

    def partition(self):
        pass

    def is_palindrome(self):
        if not self.head:
            raise Exception("Linked List is empty!")
        # could be done with lists, but appending to the beginning of a list is expensive - just as reversing afterwards would be
        elements = deque()
        reversed = deque()
        node = self.head
        while node:
            elements.append(node.data)
            reversed.appendleft(node.data)
            node = node.next
        return reversed == elements

    def len(self):
        if not self.head:
            return 0
        node = self.head
        count = 0
        while node:
            node = node.next
            count += 1
        return count

    def get_circular_loop_head(self):
        if not self.head:
            raise Exception("Linked List is empty!")
        tortoise = self.head
        hare = self.head

        while tortoise.next and hare.next.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare is tortoise:
                return hare

        return None


# TODO refactor repeated code to methods
def sum_linked_lists_reverse(linked_list_1, linked_list_2):
    first_num_digits = deque()
    node = linked_list_1.head

    while node:
        first_num_digits.appendleft(node.data)
        node = node.next

    second_num_digits = deque()
    node = linked_list_2.head
    while node:
        second_num_digits.appendleft(node.data)
        node = node.next

    decimal_place = 10 ** (len(first_num_digits) - 1)
    num_1 = 0
    for num in first_num_digits:
        num_1 += num * decimal_place
        decimal_place = int(decimal_place / 10)

    decimal_place = 10 ** (len(first_num_digits) - 1)
    num_2 = 0
    for num in second_num_digits:
        num_2 += num * decimal_place
        decimal_place = int(decimal_place / 10)

    sum_of_nums = num_1 + num_2
    reversed_digits = []

    while sum_of_nums >= 1:
        digit = sum_of_nums % 10
        reversed_digits.append(digit)
        sum_of_nums = int(sum_of_nums / 10)

    ll = LinkedList(list(reversed_digits))
    return ll


def is_intersection_present(linked_list_1, linked_list_2):
    linked_list_1_len = linked_list_1.len()
    linked_list_2_len = linked_list_2.len()

    if linked_list_1_len and linked_list_2_len:
        if linked_list_1_len >= linked_list_2_len:
            shorter = linked_list_2
            longer = linked_list_1
        else:
            shorter = linked_list_1
            longer = linked_list_2

        node1 = shorter.head
        node2 = longer.head

        while node1:
            while node2:
                if node1 is node2:
                    return True
                node2 = node2.next
            node1 = node1.next
            node2 = longer.head
    else:
        return False




