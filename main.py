from src.LinkedList import LinkedList
from src.hashTable import HashTable
import random


def fakeNames(noNames):
    result = []

    names = ["Roberto", "Armin", "Pedros", "Leonardo", "Efrain",
             "Mario", "Apoquinto", "Rodolfo", "Armando", "Dario"]
    lastnames = ["Llanes", "Zurita", "Tuz", "Buen", "Fin",
                 "Armando", "Apoquinto", "Torres", "Monsreal", "Peña"]

    for name in range(noNames):
        result.append(
            [names[random.randint(0, 9)] + ' ' + names[random.randint(0, 9)] + ' ' +
             lastnames[random.randint(0, 9)] + ' ' + lastnames[random.randint(0, 9)], name]
        )

    return result


def example1():
    table = HashTable(15)

    table.add("Roberto Carlos", "Calle 121 Cinco Colonias")
    table.add("Carlos Roberto", "Calle 121 Cinco Colonias")

    print(table.search("Roberto Carlos"))


def example2():
    table = HashTable(10)

    for key, value in fakeNames(50):
        table.add(key, value)

    print(table.printTable())


def main():
    example2()


if __name__ == '__main__':
    main()
