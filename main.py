from src.LinkedList import LinkedList
from src.hashTable import HashTable


def main():
    table = HashTable(5)

    table.addElement(2, 13)
    table.addElement(2, 23)
    table.addElement(2, 33)

    print("Test", table.getBucket(2))

    table.printTable()


if __name__ == '__main__':
    main()
