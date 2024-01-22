from sortedcontainers import SortedSet

class SmallestInfiniteSet:
    def __init__(self):
        self.s = SortedSet(range(1, 1001))

    def popSmallest(self):
        if self.s:
            x = self.s.pop(0)
            return x
        return -1  # Placeholder value when the set is empty

    def addBack(self, num):
        self.s.add(num)

# Example usage:
obj = SmallestInfiniteSet()
print(obj.popSmallest())  # Output: 1
obj.addBack(2)
print(obj.popSmallest())  # Output: 2
print(obj.popSmallest())  # Output: 3
obj.addBack(1)
print(obj.popSmallest())  # Output: 1
print(obj.popSmallest())  # Output: 4
print(obj.popSmallest())  # Output: 5
