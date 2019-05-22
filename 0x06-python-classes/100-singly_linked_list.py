#!/usr/bin/python3


class Node:
    """Node of a singly linked list.
    Private instance attribute: data:
        - property def data(self)
        - property setter def data(self, value)
    Private instance attribute: next_node:
        - property def next_node(self)
        - property setter def next_node(self, value)
    Instantiation with data and next_node.
    """

    def __init__(self, data, next_node=None):
        """Initializes the data of the node."""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieves the data from the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data into a node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node."""
        if not isinstance(value, Node) or value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Singly linked list.
    Private instance attribute: head.
    Simple instantiation.
    Public instance method: def sorted_insert(self, value).
    """

    def __init__(self):
        """Initializes the linked list."""
        self.__head = None

    def __str__(self):
        """For the print statement in the main file."""
        return str(self.__head.data)

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list."""
        new_node = Node(value)
        node = self.__head
        if self.__head is None:
            self.__head = new_node
            self.__head.__next_node = None
            return
        if node.__next_node is None:
            print(node.data)
            if value > node.data:
                node.__next_node = new_node
                new_node.__next_node = None
            elif value <= node.data:
                new_node.__next_node = node
                self.__head = new_node
            return
        while value <= node.data:
            node = node.__next_node
            if node is None:
                break
        new_node.__next_node = node
        if node is not None:
            node.__next_node = new_node
