from src.LinkedList import LinkedList, Node


class HashTable():
    def __init__(self, buckets):
        self.table = [LinkedList("->") for element in range(buckets)]

    def addElement(self, index, value):
        return self.table[index].addNode(value)

    def printTable(self):
        for bucket in range(len(self.table)):
            print(self.getBucket(bucket))

    def getBucket(self, index):
        return self.table[index].getList(self.table[index].getInitial())
