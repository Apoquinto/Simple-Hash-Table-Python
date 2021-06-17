class HashTable():
    def __init__(self, buckets):
        self.noBuckets = self.getMaxPrime(buckets)
        self.table = [[] for bucket in range(self.noBuckets)]

    def add(self, key, value):
        self.insert(self.hashFun(key), value)

    def search(self, key):
        return self.table[self.hashFun(key)]

    def hashFun(self, key):
        result = 0
        for char in str(key):
            result += ord(char)

        return result % self.noBuckets

    def insert(self, index, value):
        self.table[index].append(value)

    def printTable(self):
        for bucket in self.table:
            print(bucket)

    def getMaxPrime(self, n):
        compuests = set()
        primes = []
        for i in range(2, n+1):
            if i not in compuests:
                primes.append(i)
                compuests.update(range(i*i, n+1, i))

        return primes[-1]

    def getBucket(self, index):
        return self.table[index]
