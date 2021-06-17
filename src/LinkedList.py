from typing import NewType


class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def setNext(self, Node):
        self.nextNode = Node

    def getNextNode(self):
        return self.nextNode

    def getValue(self):
        return self.value


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.initial = self.head

    def addNode(self, value):
        newNode = Node(value)
        self.head.setNext(newNode)
        self.head = newNode

    def getInitial(self):
        return self.initial

    def getList(self, node, nodes=[]):
        if node.getNextNode() != None:
            nodes.append(node.getValue())
            self.getList(node.getNextNode(), nodes)
        else:
            nodes.append(node.getValue())

        return nodes

    def search(self, query):
        return True if query in self.getList(self.initial) else False
